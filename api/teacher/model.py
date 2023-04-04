from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TeacherDb(db.Model):
    __tablename__ = 't_teacher_tea'
    tea_id = db.Column(db.Integer, primary_key=True)
    tea_surname = db.Column(db.String(50))
    tea_firstname = db.Column(db.String(50))
    tea_login = db.Column(db.String(50))
    tea_password = db.Column(db.String(50))

    def __init__(self, row):
        self.tea_id = row[0]
        self.tea_surname = row[1]
        self.tea_firstname = row[2]
        self.tea_login = row[3]
        self.tea_password = row[4]

    def to_dict(self):
        result = {}
        if self.tea_id:
            result['tea_id'] = self.tea_id
        if self.tea_surname:
            result['tea_surname'] = self.tea_surname
        if self.tea_firstname:
            result['tea_firstname'] = self.tea_firstname
        if self.tea_login:
            result['tea_login'] = self.tea_login
        if self.tea_password:
            result['tea_password'] = self.tea_password
        return result
