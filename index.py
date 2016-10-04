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

@app.route('/user/<username>', methods=['GET'])
def getUser(username):
    user = User.query.filter(User.name == username).first()
    return app.jsonify(name=user.name)

@app.route('/user/', methods=['POST'])
def getUserPrivateInfo(username):
    username = request.args.get('username')
    secret = request.args.get('secret')
    user = User.query.filter(and_(User.name == username), User.secret == secret).first()
    if user is None:
        return "User not found", 404
    return app.jsonify(**(user.as_dict()))

@app.route('/progress/<game>/<username>')
def progress(game, username):
    user_progress = UserProgress.query.filter(and_(User.name == username, Game.name == game)).first()
    return app.jsonify(name=user.name, game=game.as_dict())

@app.route('/game/', methods=['POST'])
def getGamePrivateInfo(game):
    game_secret = request.args.get('game_secret')
    username = request.args.get('username')

    if username is None:
        return "No 'username' provided", 400
    if game_secret is None:
        return "No 'game_secret' provided", 400

    game = Game.query.filter(and_(User.name == username, Game.secret == game_secret)).first()

    if game is None:
        return "Couldn't find game", 404

    return app.jsonify(**(game.as_dict()))

@app.route('/game/', methods=['PUT'])
def newGame(game):
    game_name = request.args.get('game_name')
    username = request.args.get('username')

    if username is None:
        return "No 'username' provided", 400
    if game_name is None:
        return "No 'game_name' provided", 400

    game = Game(game)
    db_session.add(game)
    db_session.commit()

    return app.jsonify(**(game.as_dict()))

@app.route('/lock/', methods=['PUT'])
def addLock(game):
    game_secret = request.args.get('game_secret')
    username = request.args.get('username')
    lock_name = request.args.get('lock_name')
    lock_key = request.args.get('lock_key')
    lock_clue = request.args.get('lock_clue')
    lock_treasure = request.args.get('lock_treasure')

    if username is None:
        return "No 'username' provided", 400
    if game_secret is None:
        return "No 'game_secret' provided", 400
    if lock_name is None:
        return "No 'lock_name' provided", 400
    if lock_key is None:
        return "No 'lock_key' provided", 400
    if lock_clue is None:
        return "No 'lock_clue' provided", 400
    if lock_treasure is None:
        return "No 'lock_treasure' provided", 400

    game = Game.query.filter(and_(User.name == username, Game.secret == game_secret)).first()

    if game is None:
        return "Couldn't find game", 404

    lock = Lock(lock_name, lock_key, lock_clue, lock_treasure)

    return app.jsonify(**(lock.as_dict()))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
