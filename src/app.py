"""
app.py start an API to populate a database. 
"""

from flask import Flask, request, jsonify, abort
import sqlite3
import json 
import os 
import argparse

app = Flask(__name__, static_folder='./templates/html')

def db_connection(database):
    """Test connection with sqlite database 
    raise: error connection 
    return: connection to database 
    rtype: sqlite3.Connection
    """
    if not os.path.exists(database) : 
        conn = sqlite3.connect(database)
        cursor = conn.cursor() 
        sql_query = """ create table tapjoblist (
            id integer primary key autoincrement,
            user text,
            task text not null, 
            pwd text not null, 
            occ_id text not null,
            audio_sample json, 
            priority integer, 
            eta time,
            status text not null, 
            log text not null
        )
        """
        cursor.execute(sql_query) 
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.error as e:
        print(e)
    return conn

def raise_if_no_compliant(priority, task, audio_sample, status) :
    try :
        if not (0 <= int(priority) <= 2) : 
            abort(400, "priority is not in range [0,2]")
    except ValueError : 
        abort(400, "priority is not an integer")
    if task.upper() not in ["TRAP", "IL", "TAP"] : 
        abort(400, "task is not in [TRAP, IL, TAP]")
    try : 
        json.loads(audio_sample)
    except : 
        abort(400, "audio_sample is not a json")
    if status.lower() not in ["success", "pending", "failure", "retry", "abort"] :
        abort(400, "status not in [success, pending, failure, retry, abort]")


@app.route('/', defaults={'filename': 'index.html'})
@app.route("/<path:filename>") 
def index(filename) :
    """Index page for the API
    return: homepage 
    rtype: html 
    """
    return app.send_static_file(filename) 


@app.route("/api", methods=["GET"])
def query_jobs():
    """GET method when no arguments are provided. This method return 
    the content of the database.   
    return: database 
    rtype: json 
    """

    conn = db_connection(args.db)
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM tapjoblist")
    workers = [
        dict(id=row[0], user=row[1], task=row[2], pwd=row[3], occ_id=row[4], audio_sample=row[5], priority=row[6], eta=row[7], status=row[8], log=row[9])
        for row in cursor.fetchall()
    ]
    if workers is not None:
        return jsonify(workers)
    else : 
        return "database is empty"


@app.route("/api", methods=["POST"])
def create_jobs():
    """POST method when no arguments are provided in the URL. This method 
    is used to insert jobs in the database. 
    raise: error if "priority" is not an integer or not between 0 and 2. 
    task and status are also raising error if they are not respectivly in [TRAP, IL, TAP] and [success, pending, failure, retry, abort]
    return: https response code 
    rtype: str, int 
    """

    conn = db_connection(args.db)
    cursor = conn.cursor()

    user, task, pwd, occ_id, audio_sample, priority, eta, status, log = (request.form[s] for s in ('user', 'task', 'pwd', 'occ_id', 'audio_sample', 'priority', 'eta', 'status', 'log'))
    raise_if_no_compliant(priority, task, audio_sample, status)
    sql = """INSERT INTO tapjoblist (user, task, pwd, occ_id, audio_sample, priority, eta, status, log) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor = cursor.execute(sql, (user, task, pwd, occ_id, audio_sample, priority, eta, status, log))
    conn.commit()

    return f"worker created successfully", 201



@app.route("/api/<int:job_id>", methods=["PUT"])
def update_jobs(job_id):
    """PUT method when id is provided in the URL. 
    This method is mainly use to update a row in the database. 
    param: URL id 
    type: int 
    return: https response code  
    rtype: str, int  
    """

    conn = db_connection(args.db)

    def check_in_request(form_var) : 
        """Will check if a certain field is in the requests
        if it is, it will update it with the new one, 
        but if not, it will retrieve the previous one
        param: form  field 
        type : str
        return : form field
        rtype : str 
        """
        cursor = conn.cursor()
        if form_var in request.form :
            form_var = request.form[form_var]
        else : 
            cursor = conn.execute(f"select {form_var} from tapjoblist where id={job_id}")
            for row in cursor.fetchall() : 
                form_var = row[0]
        return form_var

    # TODO : change to a list 
    task = check_in_request("task")
    user = check_in_request("user")
    pwd = check_in_request("pwd")
    occ_id = check_in_request("occ_id") 
    audio_sample = check_in_request("audio_sample") 
    priority = check_in_request("priority") 
    eta = check_in_request("eta")
    status = check_in_request("status") 
    log = check_in_request("log")

    raise_if_no_compliant(priority, task,audio_sample, status)
    updated_workers = {"id": job_id,"user" : user, "task": task,"pwd": pwd,"occ_id": occ_id, "audio_sample": audio_sample,"priority" : priority, "eta" : eta, "status": status, "log" : log}
    sql = """UPDATE tapjoblist SET user=?, task=?, pwd=?, occ_id=?, audio_sample=?, priority=?, eta=?, status=?, log=? WHERE id=? """
    conn.execute(sql, (user, task, pwd, occ_id, audio_sample, priority, eta, status, log, job_id))
    conn.commit()

    return jsonify(updated_workers)


@app.route("/api/<int:job_id>", methods=["DELETE"])
def delete_jobs(job_id) :
    """DELETE method for the API. It's mainly used to delete a row in the database. 
    param: URL id 
    type: int 
    return : https response code 
    rtype : str, int 
    """

    conn = db_connection(args.db)
    sql = """ DELETE FROM tapjoblist WHERE id=? """
    conn.execute(sql, (job_id,))
    conn.commit()

    return "The worker with id: {} has been deleted.".format(job_id), 200


if __name__ == "__main__":
    """Main function. The arguments parsed are : --ip --port and --db.
    by default, IP is 0.0.0.0, port is 3002 and db is tapwebapi.db 
    """
    parser = argparse.ArgumentParser(description='Rest API')
    parser.add_argument("--ip", dest="ip", default="0.0.0.0", help="IP address")
    parser.add_argument("--port", dest="port", default="3002", help="port number")
    parser.add_argument("--db", dest="db", default="tapwebapi.db", help="path to db")
    args = parser.parse_args()
    app.run(debug=True, host=args.ip, port=args.port)
