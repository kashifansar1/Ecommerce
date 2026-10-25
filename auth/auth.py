from functools import wraps
from flask import session

def role_required(*allowed_roles):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if 'role' not in session:
                return "Login required"

            if session['role'] not in allowed_roles:
                return "Not allowed"

            return func(*args, **kwargs)

        return inner
    return wrapper