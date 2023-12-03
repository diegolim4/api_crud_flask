from flask import request, jsonify
from flask_babel import _

from app.models.user_model import update_user


def update_user_controller(user_id):
    try:
        data = request.get_json()
        name = data.get("name") # .get para everificar se "name" esta preenchido
        if name is None:
            raise ValueError("O campo 'name' e obrigatorio")
        update_user(user_id, name)
        return jsonify({"message": _("Usuário atualizado com sucesso"), "success": True}), 200
    except Exception as error:
        print('error: ', error)
        return jsonify({"error": str(error)}), 500
