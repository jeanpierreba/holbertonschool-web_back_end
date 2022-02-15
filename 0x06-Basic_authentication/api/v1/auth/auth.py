#!/usr/bin/env python3
""" contains a class to manage the API authentication. """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns True if the path is not in the list of strings """
        if path is None or excluded_paths is None:
            return True
        if path[-1] != '/':
            path = path + '/'
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ validate all requests to secure the API """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return none """
        return None
