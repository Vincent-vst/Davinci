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
            audio_sample.append(row[3])
            status.append(row[4])
    return id, task, pwd, audio_sample, status



def get_json(path) : 
    with open (path) as f : 
        data = json.load(f)
    return data

def audio_sample_parser(audio_sample) : 
    data = json.loads(audio_sample)
    print(data["name"])

id, task, pwd, audio_sample, status = get_database()
# print(audio_sample)
audio_sample_parser(audio_sample[4])
# print(get_database())

# print(get_json('../tests/example.json'))
# print_database() 

