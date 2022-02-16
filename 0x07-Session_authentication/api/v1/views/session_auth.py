#!/usr/bin/env python3
""" Module that handles all routes for the Session authentication """

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ handles all routes for the Session authentication """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if not users.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            out = jsonify(user.to_json())
            out.set_cookie(getenv('SESSION_NAME'), session_id)
            return out

@app_views.route('/auth_session/logout', methods=['DELETE'],
				 strict_slashes=False)
def logout():
	""" deletes the user session """
	from api.v1.app import auth
	if not auth.destroy_session(request):
		abort(404)
	return jsonify({}), 200
