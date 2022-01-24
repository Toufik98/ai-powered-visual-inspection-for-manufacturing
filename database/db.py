import sqlite3
from sqlite3 import Error
import csv
import os
from datetime import datetime


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def insert_card(Name,DIE,classification_result,Confidence,Bounding_box,Date):
    path = os.getcwd()
    path = path.replace(os.sep, '/')
    path = path + '/test.db'
    con = create_connection(path)
    cur = con.cursor()
    cur.execute("create table if not exists Carte (Name,DIE,Decision,Confidence,Bounding_box,Date)")
    cur.execute("insert into Carte values (?,?,?,?,?,?)", (Name,DIE,classification_result,Confidence,Bounding_box,Date))
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
    myFile.writerow(['Card_Name','DIE','Decision','Confidence','Bounding_box','Date'])
    myFile.writerows(res)
    fp.close()

if __name__ == '__main__':
    todays_date = datetime.today().strftime('%Y-%m-%d')
    insert_card("test_card_1",4,"Defected",99,"0,100,21,57",todays_date)
    insert_card("test_card_2",3,"NOT Defected",97,"0,0,0,0",todays_date)
    r = generate_report()
    print(r)
    save_report()

