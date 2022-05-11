from flask import Flask, request, jsonify, abort
import sqlite3
import json 

app = Flask(__name__, static_folder='./templates/html')

def db_connection():
    """Test connection with sqlite database 
    raise: error connection 
    return: connection to database 
    rtype: sqlite3.Connection
    """
    conn = None
    try:
        conn = sqlite3.connect("tapwebapi.db")
    except sqlite3.error as e:
        print(e)
    return conn

# TODO : might be a good idea to put all those methods in an external file 
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


@app.route("/") 
def index() :
    """Index page for the API
    return: homepage 
    rtype: html 
    """
    return "<h3>TAP web API</h3><br><a href='/api/docs/about.html'>documentation</a>"


@app.route('/api/docs/<path:filename>')
def documentation(filename):
    """Documentation page made with spinx.
    return: documentation page  
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

    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM tapjoblist")
    workers = [
        dict(id=row[0], user=row[1], task=row[2], pwd=row[3], occ_id=row[4], audio_sample=row[5], priority=row[6], eta=row[7], status=row[8])
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

    conn = db_connection()
    cursor = conn.cursor()

    user, task, pwd, occ_id, audio_sample, priority, eta, status = (request.form[s] for s in ('user', 'task', 'pwd', 'occ_id', 'audio_sample', 'priority', 'eta', 'status'))
    raise_if_no_compliant(priority, task, audio_sample, status)
    sql = """INSERT INTO tapjoblist (user, task, pwd, occ_id, audio_sample, priority, eta, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor = cursor.execute(sql, (user, task, pwd, occ_id, audio_sample, priority, eta, status))
    conn.commit()

    return f"worker created successfully", 201



@app.route("/api/<int:id>", methods=["PUT"])
def update_jobs(id):
    """PUT method when id is provided in the URL. 
    This method is mainly use to update a row in the database. 
    param: URL id 
    type: int 
    return: https response code  
    rtype: str, int  
    """
    conn = db_connection()

    def check_in_request(form_var) : 
        cursor = conn.cursor()
        if form_var in request.form :
            form_var = request.form[form_var]
        else : 
            cursor = conn.execute(f"select {form_var} from tapjoblist where id={id}")
            for row in cursor.fetchall() : 
                form_var = row[0]
        return form_var


    task = check_in_request("task")
    user = check_in_request("user")
    pwd = check_in_request("pwd")
    occ_id = check_in_request("occ_id") 
    audio_sample = check_in_request("audio_sample") 
    priority = check_in_request("priority") 
    eta = check_in_request("eta")
    status = check_in_request("status") 

    raise_if_no_compliant(priority, task,audio_sample, status)
    updated_workers = {"id": id,"user" : user, "task": task,"pwd": pwd,"occ_id": occ_id, "audio_sample": audio_sample,"priority" : priority, "eta" : eta, "status": status}
    sql = """UPDATE tapjoblist SET user=?, task=?, pwd=?, occ_id=?, audio_sample=?, priority=?, eta=?, status=? WHERE id=? """
    conn.execute(sql, (user, task, pwd, occ_id, audio_sample, priority, eta, status, id))
    conn.commit()

    return jsonify(updated_workers)


@app.route("/api/<int:id>", methods=["DELETE"])
def delete_jobs(id) :
    """DELETE method for the API. It's mainly used to delete a row in the database. 
    param: URL id 
    type: int 
    return : https response code 
    rtype : str, int 
    """

    conn = db_connection()
    sql = """ DELETE FROM tapjoblist WHERE id=? """
    conn.execute(sql, (id,))
    conn.commit()

    return "The worker with id: {} has been deleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True, port=3000)
