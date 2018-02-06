import unittest
from app.models import Pitch,User
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_vicky = User(username='Vicky',password='potato',email='vicky@mail.com')
        self.new_pitch = Pitch(name='Victoria',category='Interview',pitch='Hello, I may not be the best but I wont be',user=self.user_vicky)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.name,'Victoria')
        self.assertEquals(self.new_pitch.category,'Interview')
        self.assertEquals(self.new_pitch.pitch,'Hello, I may not be the best but I wont be')
        self.assertEquals(self.new_pitch.user,self.user_vicky)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_category(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_category('Interview')
        self.assertTrue(len(got_pitch) == 1)