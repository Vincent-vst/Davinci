import sqlite3

conn = sqlite3.connect("tapwebapi.db")

cursor = conn.cursor()
sql_query = """ create table tapjoblist (
    id integer primary key autoincrement,
    user text,
    task text not null, 
    pwd text not null, 
    occ_id text not null,
    audio_sample json, 
    priority integer, 
    eta time,
    status text not null
)

"""

# example de requete : 
# insert into tapjoblist (user, task, pwd, audio_sample, priority, eta, status) values ('vincent', 'IL', '/tmp', '{"name": "vincent"}', 2, datetime(), 'failure'); 


cursor.execute(sql_query)
