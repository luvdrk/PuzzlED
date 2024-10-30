import sqlite3
import random

def Delete_question(questionid, tablename):
    sql = sqlite3.connect("quiz.db")
    cur = sql.cursor()
    querry = "DELETE FROM "+tablename+" WHERE questionid="+questionid
    cur.execute(querry)
    sql.commit()
    sql.close()
def SelectAll_Tables():
    sql = sqlite3.connect("quiz.db")
    cur = sql.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    data = cur.fetchall()
    sql.commit()
    sql.close()
    return data

def Create_Quiz_Set(id):
    try:
        sql = sqlite3.connect("quiz.db")
        cur = sql.cursor()
        querry = "CREATE TABLE " + id + "(questionid INTEGER PRIMARY KEY,question TEXT NOT NULL, op1 TEXT, op2 TEXT, op3 TEXT, op4 TEXT, answer TEXT NOT NULL)"
        print(querry)
        cur.execute(querry)
        print("table created")
        cur.close()
        sql.commit()
        sql.close()
        return "Success"
    except sqlite3.OperationalError:

        return "sqlite3.OperationalError"

def InsertValue(questionname, op1, op2, op3, op4, answer, databasename):
    questionid = random.randrange(1000, 1000000000)
    print(questionid)
    sql = sqlite3.connect("quiz.db")
    cur = sql.cursor()
    #querry = "INSERT INTO {}(questionid, question, op1, op2, op3, op4, answer) VALUES({},{},{},{},{},{},{})".format(databasename, questionid,questionname, op1, op2, op3, op4, answer)
    #print("INSERT INTO ?(question, op1, op2, op3, op4, answer) VALUES(?,?,?,?,?,?)",(databasename, questionname, op1, op2, op3, op4, answer))
    cur.execute("INSERT INTO "+databasename+"(questionid, question, op1, op2, op3, op4, answer) VALUES(?,?,?,?,?,?,?)",(questionid,questionname, op1, op2, op3, op4, answer))
    cur.close()
    sql.commit()
    sql.close()
    print("data inserted")

def GetQuistions(tablename):
    sql = sqlite3.connect("quiz.db")
    cur = sql.cursor()
    cur.execute("SELECT * FROM "+tablename)
    datas = cur.fetchall()
    cur.close()
    sql.commit()
    sql.close()
    return datas

def DeleteTable(tablename):
    sql = sqlite3.connect("quiz.db")
    cur = sql.cursor()
    querry = "DROP TABLE "+tablename
    cur.execute(querry)
    sql.commit()
    sql.close()
    print("table deleted")