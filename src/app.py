from flask import Flask, request, jsonify, abort
import json
import sqlite3

app = Flask(__name__)


"""
description : test connection with sqlite database 
parameters : None 
type : None 
return : connection  
"""
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("tapwebapi.db")
    except sqlite3.error as e:
        print(e)
    return conn

"""
description : API method when no arguments are provided  
parameters : None 
return : error code & message 
"""
@app.route("/api", methods=["GET", "POST"])
def workers():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM tapjoblist")
        workers = [
            dict(id=row[0], user=row[1], task=row[2], pwd=row[3], audio_sample=row[4], priority=row[5], eta=row[6], status=row[7])
            for row in cursor.fetchall()
        ]
        if workers is not None:
            return jsonify(workers)

    if request.method == "POST":
        new_user = request.form["user"]
        new_task = request.form["task"]
        new_pwd = request.form["pwd"]
        new_audio_sample = request.form["audio_sample"]
        new_priority = request.form["priority"]
        # new_priority = int(new_priority)
        new_eta = request.form["eta"]
        new_status = request.form["status"]
        try :
            if not (0 <= int(new_priority) <= 2) : 
                abort(400, "priority is not in range [0,2]")
        except ValueError : 
            abort(400, "priority is not an integer")
        sql = """INSERT INTO tapjoblist (user, task, pwd, audio_sample, priority, eta, status) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (new_user, new_task, new_pwd, new_audio_sample, new_priority, new_eta, new_status))
        conn.commit()
        return f"worker created successfully", 201


"""
description : API method when table id is provided  
parameters : None 
return : error code & message
"""
@app.route("/api/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_workers(id):
    conn = db_connection()
    # cursor = conn.cursor()
    # workers = None

    # if request.method == "GET":
    #     cursor.execute("SELECT * FROM workers WHERE id=?", (id,))
    #     for row in cursor.fetchall():
    #         workers = row
    #     if workers is not None:
    #         return jsonify(workers), 200
    #     else:
    #         return "Error", 404

    if request.method == "PUT":
        # print(id)
        sql = """UPDATE tapjoblist SET user=?, task=?, pwd=?, audio_sample=?, priority=?, eta=?, status=? WHERE id=? """
        user = request.form["user"]
        task = request.form["task"]
        pwd = request.form["pwd"]
        audio_sample = request.form["audio_sample"]
        priority = request.form["priority"]
        eta = request.form["eta"]
        status = request.form["status"]
        updated_workers = {
            "id": id,
            "user" : user, 
            "task": task,
            "pwd": pwd,
            "audio_sample": audio_sample,
            "priority" : priority, 
            "eta" : eta, 
            "status": status,
        }
        conn.execute(sql, (user, task, pwd, audio_sample, priority, eta, status, id))
        conn.commit()
        return jsonify(updated_workers)

    if request.method == "DELETE":
        sql = """ DELETE FROM tapjoblist WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The worker with id: {} has been deleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=3001)
