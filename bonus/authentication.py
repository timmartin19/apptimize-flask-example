import random

from flask import Flask, Response


def authenticate(func):
    def wrapper(*args, **kwargs):
        # do your authentication
        authenticated = random.choice([True, False])
        if not authenticated:
            return Response("You're not authenticated!", status=401)
        return func(*args, **kwargs)
    return wrapper

app = Flask("authentication")


@app.route('/authenticated')
@authenticate
def some_authenticated_route():
    # At this the authentication has already been called
    return Response('Your authenticated!')