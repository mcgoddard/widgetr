from Widgetr import app
import sqlite3
from flask import g
import os.path

DATABASE = './widgetr-database.db'

def init_db():
    #with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.cursor().close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    if not os.path.isfile(DATABASE):
        init_db()
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def select(table):
    if not os.path.isfile(DATABASE):
        init_db()
    db = get_db()
    cur = db.cursor()
    query = 'SELECT * FROM hosts'
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result

def delete(table, field, value):
    if not os.path.isfile(DATABASE):
        init_db()
    db = get_db()
    cur = db.cursor()
    query = 'DELETE FROM %s where %s = %s' % (
        table,
        field,
        value
    )
    cur.execute(query)
    db.commit()

def insert(table, fields=(), values=()):
    if not os.path.isfile(DATABASE):
        init_db()
    db = get_db()
    cur = db.cursor()
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cur.execute(query, values)
    db.commit()
    id = cur.lastrowid
    cur.close()
    return id

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

