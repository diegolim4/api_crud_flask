from flask import jsonify, request
from flask_babel import _
from app.models.user_model import create_user

def insert_user_controller():
    try:
        data = request.get_json()
        name = data["name"]
        user_id = create_user(name)
        return {"id": user_id, "message": _(f"Usuário: {name} inserido com sucesso."), "success": True}, 201
    except Exception as error:
        print('Error: ',error)
        return jsonify({"error": str(error)}), 500
