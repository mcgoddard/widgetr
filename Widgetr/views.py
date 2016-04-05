"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request, render_template, redirect, url_for
from Widgetr import app
from Widgetr import data_access_layer
import json

@app.route('/')
def widgetr():
    """Renders the widgetr page."""
    port = 56988
    hosts = data_access_layer.select("hosts")
    hostnames = [el[1] for el in hosts]
    return render_template(
        'widgetr.html',
        title='Widgetr',
        year=datetime.now().year,
        hosts=json.dumps(hostnames),
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

@app.route('/delete_host/<int:host_id>', methods=['GET'])
def delete_host(host_id):
    hostname = request.args.get('hostname')
    data_access_layer.delete('hosts', 'id', host_id)
    return redirect(url_for('admin'))

@app.route('/not-a-widget', methods=['GET'])
def not_a_widget():
    return render_template('not-a-widget.html')

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )