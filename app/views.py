from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title='Welcome to Pitches!!!'
    return render_template('index.html', title=title)

@app.route('/pitch/<pitch_id>')
def pitchi(pitch_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)
    