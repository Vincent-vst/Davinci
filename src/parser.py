import sqlite3   
import json 

def db_connection() : 
    conn = None 
    try : 
        conn = sqlite3.connect('davinci.db')
    except sqlite3.error as e : 
        print(e)
    return conn

def print_database() : 
    conn = db_connection()
    with conn :
        for row in conn.execute('select * from workers').fetchall(): 
            print(row)


def get_json(path) : 
    with open (path) as f : 
        data = json.load(f)
    return data

# print(get_json('../tests/example.json'))
print_database() 
