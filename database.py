from django.db import connection

import sqlite3
def create_connection():
    connection=sqlite3.connect('memory.db')
    return connection

def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM questionsAndAnswers") 
    return cur.fetchall()

def get_ans_from_memory(question):
    rows =get_questions_and_answers()
    answer="" 
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer
              

#print(get_ans_from_memory("What is the time"))