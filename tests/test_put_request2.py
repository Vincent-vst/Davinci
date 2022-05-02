import sqlite3

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


conn = db_connection()
cursor = conn.cursor()

cursor = conn.execute("select task from tapjoblist where id=2")
for row in cursor.fetchall() : 
    task = row[0]
print(task)

#if request.method == "GET":
#    cursor = conn.execute("SELECT * FROM tapjoblist")
#    workers = [
#        dict(id=row[0], user=row[1], task=row[2], pwd=row[3], occ_id=row[4], audio_sample=row[5], priority=row[6], eta=row[7], status=row[8])
#        for row in cursor.fetchall()
#    ]
#    if workers is not None:
#        return jsonify(workers)
#    #TODO : where is else ? 


