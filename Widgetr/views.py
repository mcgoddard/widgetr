"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Widgetr import app

@app.route('/')
def widgetr():
    """Renders the widgetr page."""
    port = 56988
    return render_template(
        'widgetr.html',
        title='Widgetr',
        year=datetime.now().year,
        hosts="[ 'http://localhost:"+str(port)+"/red','http://localhost:"+str(port)+"/green','http://localhost:"+str(port)+"/blue','http://localhost:"+str(port)+"/yellow','http://localhost:"+str(port)+"/orange','http://localhost:"+str(port)+"/pink','http://localhost:"+str(port)+"/purple','http://localhost:"+str(port)+"/brown','http://localhost:"+str(port)+"/turquoise','http://localhost:"+str(port)+"/white','http://localhost:"+str(port)+"/black','http://localhost:"+str(port)+"/grey' ]",
    )

@app.route('/admin')
def admin():
    """Renders the admin page."""
    return render_template(
        'admin.html',
        title='Admin Panel',
        year=datetime.now().year,
    )

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
