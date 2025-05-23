from app.extensions import db, migrate
from datetime import datetime

class Course(db.Model):
    __tablename__ = "Course"
    id = db.Column(db.Interger)
    name = db.Column(db.String(255), nullable= False)
    code = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    update_at = db.Column(db.DateTime, default = datetime.utcnow)
    
# def __repr__(self):
#         return f'<Course {self.code} - {self.name}>'