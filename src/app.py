from flask import Flask, request, jsonify
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
        conn = sqlite3.connect("davinci.db")
    except sqlite3.error as e:
        print(e)
    return conn

"""
description : API method when no arguments are provided  
parameters : None 
return : error code & message 
"""
@app.route("/workers", methods=["GET", "POST"])
def workers():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM workers")
        workers = [
            dict(id=row[0], task=row[1], pwd=row[2], status=row[3], audio_sample=row[4])
            for row in cursor.fetchall()
        ]
        if workers is not None:
            return jsonify(workers)

    if request.method == "POST":
        new_task = request.form["task"]
        new_lang = request.form["pwd"]
        new_status = request.form["status"]
        new_audio_sample = request.form["audio_sample"]
        # new_audio_sample = str(new_audio_sample) #TODO : <-- this might crash, but idk why tho ..
        sql = """INSERT INTO workers (task, pwd, status, audio_sample) VALUES (?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (new_task, new_lang, new_status, new_audio_sample))
        conn.commit()
        return f"worker created successfully", 201


"""
description : API method when table id is provided  
parameters : None 
return : error code & message
"""
@app.route("/workers/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_workers(id):
    conn = db_connection()
    cursor = conn.cursor()
    workers = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM workers WHERE id=?", (id,))
        for row in cursor.fetchall():
            workers = row
        if workers is not None:
            return jsonify(workers), 200
        else:
            return "Error", 404

    if request.method == "PUT":
        sql = """UPDATE workers SET task=?, pwd=?, status=?, audio_sample=? WHERE id=? """
        task = request.form["task"]
        pwd = request.form["pwd"]
        status = request.form["status"]
        audio_sample = request.form["audio_sample"]
        updated_workers = {
            "id": id,
            "task": task,
            "pwd": pwd,
            "status": status,
            "audio_sample": audio_sample,
        }
        conn.execute(sql, (task, pwd, audio_sample, status, id))
        conn.commit()
        return jsonify(updated_workers)

    if request.method == "DELETE":
        sql = """ DELETE FROM workers WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The worker with id: {} has been deleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=3001)
