from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile
# from .forms import PitchForm
from flask_login import login_required
from ..models import Pitch, User
from .. import db, photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'PITCH PERFECT!'
    return render_template('index.html',title = title)

@main.route('/encouraging/pitch/')
def encouraging():
    '''
    View root page function that returns the encouraging page and its data
    '''

    pitch = Pitch.query.filter_by(category='encouraging')
    return render_template('encouraging.html',title = title, pitch = pitch)

@main.route('/funny/pitch/')
def funny():
    '''
    View root page function that returns the funny page and its data
    '''

    pitch = pitch.get_pitches()
    return render_template('funny.html',title = title, pitch = pitch)

@main.route('/life/pitch/')
def life():
    '''
    View root page function that returns the life page and its data
    '''

    pitch = pitch.get_pitches()
    return render_template('life.html',title = title, pitch = pitch)
 
@main.route('/pitch/<int:pitch_id>', methods = ['GET','POST'])
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''

    return render_template('pitch.html',id = pitch_id, pitch = pitch)    

@main.route('/pitch/pitch/new/<int:id>', methods = ['GET','POST'])
def new_pitch(id):
    form = PitchForm()
    pitch = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        new_pitch = Pitch(pitch.id,pitch)
        new_pitch.save_pitch()
        return redirect(url_for('pitch',id = pitch.id ))

    title = f'{pitch.title} pitch'
    return render_template('new_pitch.html',title = title, pitch_form=form, pitch=pitch)

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