# Section 4: Video 71 and 72 

from models.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(Username, Password):
    user = UserModel.find_by_username(Username)
    if user and safe_str_cmp(user.Password, Password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
