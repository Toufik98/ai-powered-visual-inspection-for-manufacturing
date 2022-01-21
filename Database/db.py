import sqlite3
from sqlite3 import Error
import csv
import os

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def insert_card(Name,DIE,classification_result,Date):
    path = os.getcwd()
    path = path.replace(os.sep, '/')
    path = path + '/test.db'
    con = create_connection(path)
    cur = con.cursor()
    cur.execute("create table if not exists Carte (Name,DIE,classification_result,Date)")
    cur.execute("insert into Carte values (?,?,?,?)", (Name,DIE,classification_result,Date))
    con.commit()
    con.close()

def generate_report():
    path = os.getcwd()
    path = path.replace(os.sep, '/')
    path = path + '/test.db'
    con = create_connection(path)
    cur = con.cursor()
    cur.execute("select * from carte")
    results = cur.fetchall()
    con.close()
    return results

def save_report():
    path = os.getcwd()
    path = path.replace(os.sep, '/')
    path = path + '/test.db'    
    res = generate_report()
    fp = open("report.csv", "w", newline='')
    myFile = csv.writer(fp, delimiter = ',')
    myFile.writerow(['Card_Name','DIE','classification_result','Date'])
    myFile.writerows(res)
    fp.close()

if __name__ == '__main__':


    insert_card("test_card_1",4,"Defected","2022-01-21")
    r = generate_report()
    print(r)
    save_report()

