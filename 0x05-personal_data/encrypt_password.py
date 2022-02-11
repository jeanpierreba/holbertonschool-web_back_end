#!/usr/bin/env python3
""" Encrypts passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Expects one string argument name password
    and returns a salted, hashed password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validate the provided password """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
