from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    message = 'One Minute pitch for us all'
    return render_template('index.html',message=message)

@app.route('/create/<uname>')
def create(uname):
    '''
    View page that returns a form to create your own pitch
    '''
    return render_template('create.html',uname=uname)
