"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request, render_template, redirect, url_for
from Widgetr import app
from Widgetr import data_access_layer

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

@app.route('/admin', methods=['POST'])
def submit_host():
    hostname = request.form['hostname']
    data_access_layer.insert("hosts", ["hostname"], [hostname])
    return redirect(url_for('admin'))

@app.route('/admin', methods=['GET'])
def admin():
    """Renders the admin page."""
    hosts = data_access_layer.select("hosts")
    return render_template(
        'admin.html',
        title='Admin Panel',
        year=datetime.now().year,
        hosts = hosts
    )

@app.route('/delete_host', methods=['GET'])
def delete_host():
    hostname = request.args.get('hostname')
    data_access_layer.delete('hosts', 'hostname', hostname)
    return redirect(url_for('admin'))


@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )