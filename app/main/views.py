from flask import render_template
from . import main
# from .models import review
# from .forms import ReviewForm

# Review = review.Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'PITCH PERFECT!'
    return render_template('index.html',title = title)


@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)    

# @main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     form = ReviewForm()
#     movie = get_pitch(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(id, pitch, review)
#         new_review.save_review()
#         return redirect('pitch',id = pitch.id )

#     title = f'{pitch.title} review'
#     return render_template('new_review.html',title = title, review_form=form, pitch=pitch)    