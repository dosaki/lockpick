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
    user = User(username)
    db_session.add(user)
    db_session.commit()
    return app.jsonify(**(user.as_dict()))

@app.route('/view/<username>')
def view(username):
    user = User.query.filter(User.name == username).first()
    return app.jsonify(name=user.name)

@app.route('/progress/<game>/<username>')
def progress(game, username):
    user_progress = UserProgress.query.filter(and_(User.name == username, Game.name == game)).first()
    return app.jsonify(name=user.name, game=game.as_dict())

@app.route('/new/<game>')
def newGame(game):
    game = Game(game)
    db_session.add(game)
    db_session.commit()
    return app.jsonify(**(game.as_dict()))

@app.route('/addLock/<game>')
def addLock(game):
    secret = request.args.get('secret')
    username = request.args.get('username')
    
    user = User.query.filter(and_(User.secret == secret, User.name == username)).first()
    game = Game.query.filter(Game.name == game).first()
    return app.jsonify(**(game.as_dict()))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
