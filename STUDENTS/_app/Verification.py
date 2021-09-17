from werkzeug.security import safe_str_cmp
from models.User import UserModel

def authenticate(Username, Password):
    user = UserModel.Search_By_Username(Username)
    if user and safe_str_cmp(user.Password, Password):
        return user

def identity(payload):
    User_id = payload['identity']
    return UserModel.Search_By_id(User_id)

