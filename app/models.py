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