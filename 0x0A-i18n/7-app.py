#!/usr/bin/env python3

""" basic Flask app """

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

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
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """ determine the best match """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in Config.LANGUAGES:
            return locale
    locale = request.headers.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
	""" get timezone selector """
	try:
		if request.args.get('timezone'):
			time_zone = request.args.get('timezone')
			pytz.timezone(time_zone)
		elif g.user and g.user.get('timezone'):
			time_zone = g.user.get('timezone')
			pytz.timezone(time_zone)
		else:
			time_zone = app.config["BABEL_DEFAULT_TIMEZONE"]
			pytz.timezone(time_zone)
	except pytz.exceptions.UnknownTimeZoneError:
		time_zone = "UTC"
	return time_zone	


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def index():
    """ returns the index """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
