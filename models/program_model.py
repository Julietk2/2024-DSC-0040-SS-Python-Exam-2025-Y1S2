from app.extensions import db, migrate
from datetime import datetime

class Program(db.Model):
    __tablename__="Program"
    id = db.Column(db.Interger )
    name = db.Column(db.String(255),nullable = False),
    description = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime , default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)