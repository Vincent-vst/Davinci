import sqlite3

conn = sqlite3.connect("davinci.db")

cursor = conn.cursor()
# sql_query = """ CREATE TABLE book (
#     id integer PRIMARY KEY,
#     author text NOT NULL,
#     language text NOT NULL,
#     title text NOT NULL
# )"""
sql_query = """ create table workers (
    id integer primary key, 
    task text not null, 
    pwd text not null, 
    status text not null
)

"""
cursor.execute(sql_query)
