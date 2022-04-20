import sqlite3   

def db_connection() : 
    conn = None 
    try : 
        conn = sqlite3.connect('davinci.db')
    except sqlite3.error as e : 
        print(e)
    return conn

conn = db_connection()

with conn :
    for row in conn.execute('select * from workers').fetchall(): 
        print(row)


