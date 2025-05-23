from flask import Blueprint,request,jsonify
from app.extensions import db, migrate
from app.status_codes import  HTTP_400_BAD_REQUEST,HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
from datetime import datetime
from app.models.program_model import Program

program = Blueprint('program' , __name__ , url_prefix='/api/v1/program')

@program.route('/register', methods=['POST'])
def create_program():
    data = request.json()
    if not name or not description :
        return jsonify({"error": "All fields are required"}), HTTP_400_BAD_REQUEST
    
    name = data.get('name')
    code = data.get('code')
    description = data.get('description')
    
    if Program.query.filter_by(code=code).first():
        return jsonify({"error": "Code already registered"}), HTTP_400_BAD_REQUEST,
    
    try:
        new_program = Program(
            id = new_program.id,
            name = new_program.name,
            description = new_program.description
        )
        db.session.add(new_program)
        db.session.commit()
        
        return jsonify ({
            "message": new_program.name + "has been created",
            "program":{
                "id": new_program.id,
                "name":new_program.name,
                "code":new_program.code
            }
                
            }
        ),HTTP_201_CREATED
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
        
        
#  update program

@program.put('/<int:program_id>',)
def update_program(program_id):
    try:
        program = program.query.get(program_id)
        if not program:
             return jsonify({"error": "program not found"}),HTTP_400_BAD_REQUEST
         
        data = request.json
        program.name = data.get('name', program.name)
        program.description = data.get('description', program.description)
        
        db.session.commit()

        return jsonify({
             "message": "program updated successfully",
             "program": {
                 "id": program.id,
                 "name":program.name,
                 "description":program.description
             }
             }
        ),HTTP_200_OK
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})   
        
     
         
        
        
 