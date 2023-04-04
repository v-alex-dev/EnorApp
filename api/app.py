import traceback

from flask import Flask, jsonify
from teacher.model import TeacherDb
import psycopg2

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


@app.route('/all_teacher', methods=['GET'])
def get_all_teachers():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM t_teacher_tea")

        rows = cur.fetchall()
        teachers = [TeacherDb(row).to_dict() for row in rows]

        return jsonify(teachers)
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})


@app.route('/teacher_by_id/<int:id>', methods=['GET'])
def get_teacher_by_id(id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * "
                    "FROM t_teacher_tea "
                    "WHERE tea_id = %s", (id,))
        rows = cur.fetchall()
        teacher = [TeacherDb(row).to_dict() for row in rows]

        return jsonify(teacher)
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})
