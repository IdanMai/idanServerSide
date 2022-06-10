from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def landing_page():  # put application's code here
    return redirect(url_for('home_page'))


@app.route('/home')
def home_page():  # put application's code here
    return render_template('home.html')


@app.route('/contact')
def contact_page():  # put application's code here
    return render_template('contact.html')


@app.route('/assignment3_1')
def assignment_page():  # put application's code here
    db_user_name = 'shay'  # change this to ted or someting to see the if statemant
    db_web_cost = 195354.45712
    db_subject = 'Songs'
    db_top4_songs = ('In The Beginning - knaan', 'Fix You - coldplay',
                     'Ill make a man - Mulan', 'Latinos - Proyecto Uno')
    db_rest_of_songs = ('macarena', 'thunderstruck', 'oops i did it again', 'sk8er boy',
                        'bye bye bye', 'i want it that way', 'ice ice baby')
    return render_template('assignment3_1.html',
                           user_name=db_user_name,
                           web_cost=db_web_cost,
                           subject=db_subject,
                           top4=db_top4_songs,
                           rest=db_rest_of_songs)


if __name__ == '__main__':
    app.run()
