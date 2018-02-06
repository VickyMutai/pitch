from flask_wtf import FlaskForm
from wtforms import StringField,RadioField, TextAreaField, SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    name = StringField('Authors Name', validators=[Required()])
    category = SelectField('Pick Category here',choices=[('inspiration','Inspiration'),
                                                        ('pick-up','Pick Up Lines'),
                                                        ('interview','Interview Pitch'),
                                                        ('product','Product Pitch'),
                                                        ('promotion','Promotion Pitch')], validators=[Required()])
    pitch = TextAreaField('Write your Pitch here', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')