from flask import Flask, Blueprint,request,jsonify
from app.status_codes import  HTTP_400_BAD_REQUEST,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_200_OK
from app.extensions import db
from datetime import datetime
from app.models.course_model import Course

course = Blueprint('course', __name__, url_prefix='/api/v1/course')

# Create a new student
@course.route('/register', methods=['POST'])
def create_course():
    data = request.json()
    if not code or not name:
        return jsonify({"error": "All fields are required"}), HTTP_400_BAD_REQUEST
    
    name = data.get('name')
    code = data.get('code')
    description = data.get('description')
    
    if Course.query.filter_by(code=code).first():
        return jsonify({"error": "Code already registered"}), HTTP_400_BAD_REQUEST
    
    try:
        new_course = Course (
        name = name,
        code = code )
        
        
        
        db.session.add(new_course)
        db.session.commit()
        
        return jsonify ({
            "Message": " new_course.name  +   has been created",
            "course":{
                "id": new_course.id,
                "name":new_course.name,
                "code":new_course.code
            }
        }),HTTP_201_CREATED
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
        
        
        
    
        
    