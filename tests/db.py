import sqlite3

conn = sqlite3.connect("davinci.db")

cursor = conn.cursor()
sql_query = """ create table workers (
    id integer primary key, 
    task text not null, 
    pwd text not null, 
    status text not null, 
    audio_sample text not null
)

"""
cursor.execute(sql_query)
