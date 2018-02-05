from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch
from .forms import PitchForm
from flask_login import login_required

#views
@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    title = 'One Minute Pitch'
    return render_template('index.html',title=title)

@main.route('/create/<uname>', methods = ['GET','POST'])
@login_required
def create(uname):
    '''
    View page that returns a form to create your own pitch
    '''
    form = PitchForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        pitch_data = form.pitch.data
        new_pitch = Pitch(name,category,pitch_data)
        new_pitch.save_pitch()
        #return redirect(url_for('pitch',uname=uname))

    pitch = Pitch.get_pitch(uname)
    title = 'One Minute Pitch'
    return render_template('create.html',pitch=pitch,title=title,pitch_form=form,uname=uname)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)