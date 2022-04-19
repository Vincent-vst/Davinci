from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("davinci.db")
    except sqlite3.error as e:
        print(e)
    return conn

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


@app.route("/workers/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_workers(id):
    conn = db_connection()
    cursor = conn.cursor()
    workers = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM workers WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            workers = r
        if workers is not None:
            return jsonify(workers), 200
        else:
            return "Not found", 404

    if request.method == "PUT":
        sql = """UPDATE workers 
                SET task=?,
                    pwd=?,
                    status=?,
                    audio_sample=?
                WHERE id=? """

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
        conn.execute(sql, (task, pwd, status, id))
        conn.commit()
        #TODO : send lorem ipsum to \\garros\STAGIAIRES 
        return jsonify(updated_workers)

    if request.method == "DELETE":
        sql = """ DELETE FROM workers WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The worker with id: {} has been deleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True, port=3002)
