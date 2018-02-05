from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())    
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'



class Pitch:
    all_pitch = []
    def __init__(self,name,category,pitch):
        self.name = name
        self.category = category
        self.pitch = pitch

    def save_pitch(self):
        Pitch.all_pitch.append(self)

    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitch.clear()

    @classmethod
    def get_pitch(cls,uname):
        response = []

        for pitch in cls.all_pitch:
                response.append(pitch)
        return response