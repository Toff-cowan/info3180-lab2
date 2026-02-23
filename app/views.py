import datetime
from app import app
from flask import render_template, request, redirect, url_for, flash


def format_date_joined(date):
    """Given a date, return it formatted as Month, Year (e.g. Feb, 2021)."""
    return date.strftime("%b, %Y")


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Christoff Cowan")


@app.route('/profile')
def profile():
    date_joined = datetime.date(2019, 2, 7)  
    date_formatted = format_date_joined(date_joined)
    return render_template(
        'profile.html',
        full_name="Christoff Cowan",
        username="ccowan",
        location="Kingston, Jamaica",
        date_joined=date_formatted,
        bio="Software developer with a passion for creating innovative solutions. Experienced in Python, JavaScript, and web development. Looking forward to connecting with like-minded professionals and contributing to exciting projects.",
        posts_count=7,
        following_count=100,
        followers_count=250,
    )

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
