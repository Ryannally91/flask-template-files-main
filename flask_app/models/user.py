from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']


# CREATE model

    @classmethod
    def create_user(cls, data):
        # data = {
        #     'first_name' : "Tony",
        #     'last_name' : 'Hawk'
        # }
        query = """
        INSERT INTO users (first_name, last_name)
        VALUES (%(first_name)s, %(last_name)s)
        ;"""
        return connectToMySQL('users_read_books').query_db(query, data)

# READ model

    @classmethod
    def get_all_users(cls):
        query = """
        SELECT *
        FROM users;
        ;"""
        result = connectToMySQL('users_read_books').query_db(query)
        # print('LIST OF USERS', result)
        users = []
        for row in result:
            users.append(cls(row))
        # print("Users!!!!!!!!!!!", users)
        return users

    @classmethod
    def get_user_by_id(cls, id):
        data = { 'id' : id }
        query="""
        SELECT * 
        FROM users
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL('users_read_books').query_db(query, data)
        print('********', result)

        the_row = result[0]
        print('********', the_row)

        instance_of_user = cls(the_row)
        print('********', instance_of_user)
        return instance_of_user 

# UPDATE model

    @classmethod
    def update_user(cls, data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL('users_read_books').query_db(query, data)
        return result

# DELETE model

    @classmethod
    def delete_user(cls,id):
        data = { 'id' : id }
        query = """
        DELETE FROM users
        WHERE id = %(id)s
        ;"""
        return connectToMySQL('users_read_books').query_db(query, data)