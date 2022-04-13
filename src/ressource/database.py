from flask_restful import Resource 
import sqlite3  

class Database(Resource): 
    def get(self) : 
        con = sqlite3.connect('davinci.db') 
        cur = con.cursor() 
        
        with con : 
            cur.execute('select * from workers')
            # print(cur.fetchall())
            # return cur.fetchall() 
            return cur.execute(f"insert into workers values (4, 'TRAP', '/home/usr', 'bea2022', 'success')")
        # return "test" 

# con = sqlite3.connect('davinci.db') 
# cur = con.cursor() 
# with con:
#     cur.execute("SELECT * FROM workers")
# #     print(cur.fetchall())
# def insert_db(id, task, pwd, occurence_id, status): 
#     cur.execute(f"insert into workers values ({id}, '{task}', '{pwd}', '{occurence_id}', '{status}')")


