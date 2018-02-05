from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
class PitchForm(FlaskForm):
    name = StringField('Authors Name', validators=[Required()])
    category = StringField('Pitch Category', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')