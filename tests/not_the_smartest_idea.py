import requests 
 #  
@app.route("/api/<int:id>", methods=["PUT"])
def update_jobs(id):
    

   conn = db_connection()

    if request.method == "PUT":
       
        if user.isset() : 
            user = request.form["user"] 
        else : 
            user = "select user from tapjoblist where id=" + id 

        if task.isset():
            task = request.form["task"]
        else :
            task = "select task from tapjoblist where id=" + id 

        #TODO faire pareil pour : 
        # task = request.form["task"]
        # pwd = request.form["pwd"]
        # occ_id = request.form["occ_id"]
        # audio_sample = request.form["audio_sample"]
        # priority = request.form["priority"]
        # eta = request.form["eta"]
        # status = request.form["status"]

        
    

        sql = "udpate tapjoblist set user=" + user + "task=" + task + "pwd=" + pwd + "occ_id" + occ_id + "audio_sample=" + audio_sample + "priority=" + priority + "eta=" + eta + "status=" + status + "where id=" +id 



        conn.execute (sql)
        conn.commit()
        return "success", 200 


