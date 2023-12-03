from flask import Blueprint, request
from app.controller.insert_ctrl import insert_user_controller
from app.controller.get_ctrl import get_users_controller
from app.controller.delete_ctrl import delete_user_controller
from app.controller.update_ctrl import update_user_controller

insert_user_bp = Blueprint('insert_user', __name__)
get_users_bp = Blueprint('get_users', __name__)
delete_user_bp = Blueprint('delete_user', __name__)
update_user_bp = Blueprint('update_user', __name__)

@insert_user_bp.route('/api/insert_user', methods=['POST'])
def user_insert_route():
    return insert_user_controller()

@get_users_bp.route('/api/all_users', methods=['GET'])
def user_get_route():
    return get_users_controller()

@delete_user_bp.route('/api/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return delete_user_controller(user_id)

@update_user_bp.route('/api/update_user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    return update_user_controller(user_id)
