from flask import request, jsonify
from flask_babel import _
from app.models.user_model import delete_user


def delete_user_controller(user_id):
    try:
        delete_user(user_id)
        return jsonify({"message": _("Usuário deletado com sucesso"), "success": True}), 200
    except Exception as error:
        print('error: ', error)
        return jsonify({"error": str(error)}), 500
