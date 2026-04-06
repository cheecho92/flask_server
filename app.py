from flask import Flask, request, redirect, session
from auth import handle_tokens, url_parser
from utils import random_string_generator
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET')

@app.route('/twitch/auth')
async def twitch_auth():
    state = random_string_generator()
    session['state'] = state
    auth_uri = url_parser(twitch, state)
    return redirect(auth_uri)


@app.route('/spotify/auth')
async def spotify_auth():
    state = random_string_generator()
    session['state'] = state
    auth_uri = url_parser(spotify, state)
    return redirect(auth_uri)

@app.route('/twitch/callback')
async def twitch_callback():
    code = request.args.get('code')
    state = request.args.get('state')

    if state != session['state']:
        return "State mismatch", 400
    
    handle_tokens(twitch, code)
    return "Twitch auth complete. Bitch."


@app.route('/spotify/callback')
async def spotify_callback():
    code = request.args.get('code')
    state = request.args.get('state')

    if state != session['state']:
        return "State mismatch", 400
    
    handle_tokens(spotify, code)
    return "Spotify auth complete. Bitch."


@app.route('/overlay/<streamer>')
async def overlay(streamer):
    return f"Overlay for {streamer}"