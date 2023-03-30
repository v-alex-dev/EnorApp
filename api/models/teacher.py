from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teacher(db.Model):
    __tablename__ = 't_teacher_tea'
    tea_id = db.Column(db.Integer, primary_key=True)
    tea_first_name = db.Column(db.String(50))
    tea_last_name = db.Column(db.String(50))
    tea_login = db.Column(db.String(50))
    tea_password = db.Column(db.string(50))

    def to_dict(self):
        return {
            'id': self.tea_id,
            'surname': self.tea_first_name,
            'firstname': self.tea_last_name,
            'login': self.tea_login,
            'password': self.tea_password
        }
