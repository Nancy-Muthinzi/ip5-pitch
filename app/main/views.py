from flask import render_template
from . import main
# from .models import review
# from .forms import ReviewForm
from flask_login import login_required

# Review = review.Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'PITCH PERFECT!'
    return render_template('index.html',title = title)


@main.route('/pitch/<int:pitch_id>', methods = ['GET','POST'])
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)    

# @login_required
# def new_review(id):