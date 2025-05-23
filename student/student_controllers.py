from flask import Blueprint, request, jsonify
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_200_OK
from app.models.student_model import Student  # Import the Student model
from app.extensions import db
from datetime import datetime

# Student blueprint
student = Blueprint('student', __name__, url_prefix='/api/v1/students')

# Create a new student
@student.route('/register', methods=['POST'])
def create_student():
    data = request.json
    if not first_name or not last_name or not contact:
        return jsonify({"error": "All fields are required"}), HTTP_400_BAD_REQUEST

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    course = data.get('course')
    contact = data.get('contact')
    
    
    if Student.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), HTTP_400_BAD_REQUEST

    try:
        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            course=course,
            contact=contact
        )

        db.session.add(new_student)
        db.session.commit()
        
        return jsonify({
            "message": new_student.get_full_name + "created successfully",
            "student": {
                "id": new_student.id,
                "first_name": new_student.first_name,
                "last_name": new_student.last_name,
                "email": new_student.email,
                "course": new_student.course,
                "contact": new_student.contact,
                "created_at": new_student.created_at,
                 "updated_at": new_student.updated_at
            }
        }),HTTP_201_CREATED


    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
    
    #  Get all students
    
@student.get('/get_all_students')
def get_all_students():
    
    
    try:
        students = Student.query.all()
        students_data = []
        
        for student in students:
         student.info = {
            "id":  student.id,
            "name":  student.name,
            "email":  student.email,
            "contact": student.contact,
            "created_at": student.created_at,
            "updated_at": student.updated_at
            
        }
        students_data.append(student.info)
        
        return jsonify({
            "message": "Students retrieved successfully",
            "student": student.info
        }), HTTP_200_OK
        
    except Exception as e:
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
        
    
@student.delete('/<int:student_id>',)
def delete_student(student_id):
    try:
        student = Student.query.get(student_id)
        
        if not student:
             return jsonify({"error": "student not found"}), HTTP_400_BAD_REQUEST

        db.session.delete(student)
        db.session.commit()

        return jsonify({"message": "student deleted successfully"}), HTTP_400_BAD_REQUEST


    except Exception as e:
     db.session.rollback()
    return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR