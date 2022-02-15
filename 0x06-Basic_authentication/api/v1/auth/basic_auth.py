#!/usr/bin/env python3
""" conatins BasicAuth class to manage API """

from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """ conatins BasicAuth class to manage API authentication """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization """
        if (isinstance(authorization_header, str) and
                authorization_header.startswith('Basic ')):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of a Base64 string """
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ hat returns the user email and password from the Base64 """
        if (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ":" in decoded_base64_authorization_header):
            data = decoded_base64_authorization_header.split(":", 1)
            return (data[0], data[1])
        return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password """
        if (user_email and user_pwd and isinstance(user_email, str) and
                isinstance(user_pwd, str)):
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance """
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(b64)
        credentials = self.extract_user_credentials(decode)
        user = self.user_object_from_credentials(
            credentials[0], credentials[1])
        return user
