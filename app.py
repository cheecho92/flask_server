from flask import Flask, request, redirect, session
from winston_shared.auth import exchange_code, url_parser, save_tokens, generate_headers
from configs import twitch, spotify
from utils import random_string_generator, authenticated_user
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET')

@app.route('/twitch/auth')
def twitch_auth():
    state = random_string_generator()
    session['state'] = state
    auth_uri = url_parser(twitch, state)
    return redirect(auth_uri)


@app.route('/spotify/auth')
def spotify_auth():
    state = random_string_generator()
    session['state'] = state
    auth_uri = url_parser(spotify, state)
    return redirect(auth_uri)

@app.route('/twitch/callback')
def twitch_callback():
    code = request.args.get('code')
    state = request.args.get('state')

    if state != session['state']:
        return "State mismatch", 400

    response = exchange_code(twitch, code)
    twitch.access_token = response["access_token"]
    twitch.refresh_token = response["refresh_token"]
    twitch.channel_name = authenticated_user(twitch.access_token, twitch.client_id)
    session['username'] = twitch.channel_name
    save_tokens(twitch.channel_name, response)
    twitch.headers = generate_headers(twitch)
    return "Twitch auth complete. Bitch."


@app.route('/spotify/callback')
def spotify_callback():
    code = request.args.get('code')
    state = request.args.get('state')

    if state != session['state']:
        return "State mismatch", 400

    response = exchange_code(spotify, code)
    spotify.access_token = response["access_token"]
    spotify.refresh_token = response["refresh_token"]
    save_tokens(f"_spotify", response)
    spotify.headers = generate_headers(spotify)
    return "Spotify auth complete. Bitch."


@app.route('/overlay/<streamer>')
def overlay(streamer):
    return f"Overlay for {streamer}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)