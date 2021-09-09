from flask_app.config.mysqlconnection import connectToMySQL
DB = 'friends_schema'
class Friendship:
    def __init__(self, data):
        self.friends_first_name = data['friends_first_name']
        self.friends_last_name = data['friends_last_name']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    @classmethod
    def get_all(cls):
        query = "SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_first_name, users.last_name as friends_last_name FROM users JOIN friendships ON users.id = friendships.user_id LEFT JOIN users as users2 ON users2.id = friendships.friend_id ORDER BY first_name;"
        result = connectToMySQL(DB).query_db(query)
        friendships = []
        for friend in result:
            friendships.append(cls(friend))
        return friendships

    @classmethod
    def save_friendship(cls, data):
        query = "INSERT INTO friendships(user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s); "
        return connectToMySQL(DB).query_db(query, data)
