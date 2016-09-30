from flask import Flask

from datasource.database import init_db
from datasource.database import db_session
from datasource.models import User

app = Flask(__name__)
init_db()

@app.route('/unlock/<key>')
def unlock(key):
    return "Yay"

@app.route('/register/<username>')
def register(username):
    u = User(username)
    db_session.add(u)
    db_session.commit()
    return app.jsonify(**(u.as_dict()))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
