from wtforms import StringField,PasswordField,BooleanField,SubmitField
class LoginForm(FlaskForm):
    email = stringField('Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')