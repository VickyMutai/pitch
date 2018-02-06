from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,User
from .forms import PitchForm,UpdateProfile
from flask_login import login_required,current_user
from .. import  db,photos

#views
@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    title = 'One Minute Pitch'
    return render_template('index.html',title=title, pitches=pitches)

@main.route('/create/new', methods = ['GET','POST'])
@login_required
def create():
    '''
    View page that returns a form to create your own pitch
    '''
    form = PitchForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        pitch = form.pitch.data
        new_pitch = Pitch(name=name,category=category,
                          pitch=pitch)
        
        #save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
    title = 'One Minute Pitch'
    return render_template('create.html',title=title,pitch_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
