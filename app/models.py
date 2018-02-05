from . import db
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

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