import sqlite3   
import json 

def db_connection() : 
    conn = None 
    try : 
        conn = sqlite3.connect('example.db')
    except sqlite3.error as e : 
        print(e)
    return conn

def get_database() : 
    conn = db_connection()
    # db = []
    # task = []
    id, task, pwd, audio_sample, status = ([] for i in range(5))
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
    return str(data)


id, task, pwd, audio_sample, status=get_database()


def parse_audio_sample(audio_sample): 
    audio_sample  = audio_sample[:-1]
    # print(type(audio_sample))
    # audio_sample = eval(audio_sample)
    # print(type(audio_sample))
    # dictio = eval(audio_sample)
    results = json.loads(audio_sample.replace("'", '"'))
    print(results['name'])

parse_audio_sample(audio_sample[10])
# print(audio_sample[10].replace("'", '"'))
# print(task)
