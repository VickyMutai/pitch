from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    title = 'One Minute Pitch'
    return render_template('index.html',title=title)

@app.route('/create/<uname>')
def create(uname):
    '''
    View page that returns a form to create your own pitch
    '''
    title = 'One Minute Pitch'
    return render_template('create.html',title=title,uname=uname)
