from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import MONGO, LOGIN_MANAGER
from app.mongo_repository import MongoRepository
from app.core import BaseModel


class User(UserMixin, BaseModel):
    _collection = MONGO.db.auth_users
    username: str
    fname: str
    lname: str
    email: str
    password_hash: str
    
    
    def __init__(self, data=None):
        super(User, self).__init__(data=data)
        if data:
            self.__dict__.update(data)
            # self.username = data.get('username', '')
            # self.fname = data.get('fname', '')
            # self.lname = data.get('lname', '')
            # self.email = data.get('email', '')
            # self.password_hash = data.get('password_hash', '')
    
    @classmethod
    def find_by_username(cls, username):
        query = MongoRepository.find_one(cls, {'username': username})
        if query is None:
            return None
        return cls(data=query)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    
@LOGIN_MANAGER.user_loader
def load_user(user_id):
    user = User.find_by_username(user_id)
    return user
