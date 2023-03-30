from flask import Flask, jsonify, Response
import psycopg2

#import model
from models.teacher import Teacher

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="enorapp",
    user="alex",
    password="Crash159357"
)


@app.route('/')
def home():
    return "hello world"


@app.route('/teacher', methods=['GET'])
def get_teacher():
    cur = conn.cursor()
    cur.execute("SELECT *"
                "FROM t_teacher_tea")

    teachers = cur.fetchall()
    cur.close()


    return Response(jsonify(teachers))
