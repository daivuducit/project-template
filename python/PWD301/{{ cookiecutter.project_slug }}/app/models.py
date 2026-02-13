# Mock data models

class User:
    _users = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
    ]
    
    @classmethod
    def get_all(cls):
        return cls._users
    
    @classmethod
    def get_by_id(cls, user_id):
        for user in cls._users:
            if user['id'] == user_id:
                return user
        return None