# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# DB 연동

import sqlite3

def db_create():
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    
    # Create table
    cur.execute('''CREATE TABLE stocks
                   (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    con.commit()
    con.close()

if __name__ == "__main__":
    db_create()