class Pitch:
    all_pitch = []
    def __init__(self,category,pitch):
        self.category = category
        self.pitch = pitch

    def save_pitch(self):
        Pitch.all_pitch.append(self)

    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitch.clear()