import sqlite3 

con = sqlite3.connect('../davinci.db') 
cur = con.cursor() 

def print_db(): 
    for row in cur.execute('select * from workers') : 
        print(row) 

def insert_db(id, task, pwd, occurence_id, status): 
    cur.execute(f"insert into workers values ({id}, '{task}', '{pwd}', '{occurence_id}', '{status}')")

def delete_row(id) : 
    cur.execute(f"delete from workers where id={id}") 


