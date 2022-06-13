#!/usr/bin/env python3

""" basic Flask app """

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Babel configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_user() -> dict:
	""" returns a user dictionary or None """
	user_logged = request.args.get('login_as')
	if user_logged and int(user_logged) in users:
		return users[int(user_logged)]
	return None


@app.before_request
def before_request():
	""" find a user if any """
	if get_user():
		g.user = get_user()


@babel.localeselector
def get_locale():
    """ determine the best match """
    if request.args.get('locale'):
        if request.args.get('locale') in Config.LANGUAGES:
            return request.args.get('locale')
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def index():
    """ returns the index """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
