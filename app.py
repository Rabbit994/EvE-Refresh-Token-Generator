import os

from flask import Flask, request, redirect
from dotenv import load_dotenv
from preston import Preston

load_dotenv()
app = Flask(__name__)

@app.route('/')
def hello():
    preston = Preston(
        user_agent = os.environ['USER_AGENT'],
        client_id = os.environ['CLIENT_ID'],
        client_secret = os.environ['CLIENT_SECRET'],
        callback_url = os.environ['CALLBACK_URL'],
        scope = os.environ['SCOPES'].replace(' ','%20')
    )
    if request.args.get('code') is None:
        return redirect(location=preston.get_authorize_url(), code=302)
    else:
        code = request.args.get('code')
        auth = preston.authenticate(code=code)
        refresh_token = auth.refresh_token
        return f"<html><h2>Your refresh token is: {refresh_token}</h2><br/>Please note this token should be kept secret as it will give access to API as your character.</html>"
