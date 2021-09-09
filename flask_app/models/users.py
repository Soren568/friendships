from flask_app.config.mysqlconnection import connectToMySQL
DB = 'friends_schema'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name) VALUES (%(first_name)s,%(last_name)s);"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(DB).query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users

