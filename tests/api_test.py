from flask import Flask, request, jsonify, abort
import json 

app = Flask(__name__)

# TODO : might be a good idea to put all those methods in an external file 
def raise_if_no_compliant(priority, task, status) :
    try :
        if not (0 <= int(priority) <= 2) : 
            abort(400, "priority is not in range [0,2]")
    except ValueError : 
        abort(400, "priority is not an integer")
    if task.upper() not in ["TRAP", "IL", "TAP"] : 
        abort(400, "task is not in [TRAP, IL, TAP]")
    if status.lower() not in ["success", "pending", "failure", "retry", "abort"] :
        abort(400, "status not in [success, pending, failure, retry, abort]")


@app.route("/api", methods=["POST"])
def create_jobs():

    audio = request.form["audio"]
    try : 
        json.loads(audio)
    except :
        abort(400, "not a json")

    return f"type audio  : {type(audio)}\ncontent : {audio}", 201


if __name__ == "__main__":
    app.run(debug=True, port=3000)
