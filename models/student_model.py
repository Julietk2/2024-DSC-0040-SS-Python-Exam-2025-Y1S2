from flask import Flask
from app.extensions import db, migrate
from datetime import datetime

class Student(db.Model):
    __tablename__= "Student"
    id = db.Column(db.Interger, )
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    course = db.Column(db.String(255), nullabe = False)
    contact = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime , default = datetime.utcnow),
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)


def get_full_name(self):
        return f"{self.first_name} {self.last_name}"