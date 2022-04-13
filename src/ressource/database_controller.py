import sqlite3 

con = sqlite3.connect('../../davinci.db') 
cur = con.cursor() 

def print_db(): 
    for row in cur.execute('select * from workers') : 
        print(row) 

