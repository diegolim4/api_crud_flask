from flask import current_app

CREATE_USER_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);"
)

INSERT_USER_RETURN_ID = "INSERT INTO users (name) VALUES (%s) RETURNING id;"

SELECT_ALL_USER = "SELECT * FROM users;"

DELETE_USER_BY_ID = "DELETE FROM users WHERE id = %s;"

UPDATE_USER_BY_ID = "UPDATE users SET name = %s WHERE id = %s;"


def create_user(name):
    with current_app.db_connection:
        with current_app.db_connection.cursor() as cursor:
            cursor.execute(CREATE_USER_TABLE)
            cursor.execute(INSERT_USER_RETURN_ID, (name,))
            user_id = cursor.fetchone()[0]
    return user_id


def get_users():
    with current_app.db_connection:
        with current_app.db_connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_USER)
            users = cursor.fetchall()
    return users


def delete_user(user_id):
    with current_app.db_connection:
        with current_app.db_connection.cursor() as cursor:
            cursor.execute(DELETE_USER_BY_ID, (user_id,))
    return


def update_user(user_id, name):
    with current_app.db_connection:
        with current_app.db_connection.cursor() as cursor:
            cursor.execute(UPDATE_USER_BY_ID, (name, user_id))
    return
