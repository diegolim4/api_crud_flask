from flask import request, jsonify
from app.models.user_model import get_users


def get_users_controller():
    try:
        users = get_users()
        formatted_users = [{"id": user[0], "name": user[1]} for user in users]
        return {"users": formatted_users, "success": True}, 200
    except Exception as error:
        print('error:', error)
        return jsonify({"error": str(error)}), 500
