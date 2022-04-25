import sqlite3   
import json 

def db_connection() : 
    conn = None 
    try : 
        conn = sqlite3.connect('davinci.db')
    except sqlite3.error as e : 
        print(e)
    return conn

def get_database() : 
    conn = db_connection()
    id, task, pwd, audio_sample, status  = ([] for i in range(5))
    with conn :
        for row in conn.execute('select * from workers').fetchall(): 
            id.append(row[0])
            task.append(row[1])
            pwd.append(row[2])
            status.append(row[3])
            audio_sample.append(row[4])
    return id, task, pwd, audio_sample, status



def get_json(path) : 
    with open (path) as f : 
        data = json.load(f)
    return data

id, task, pwd, audio_sample, status = get_database()
print(audio_sample)
# print(get_database())

# print(get_json('../tests/example.json'))
# print_database() 

