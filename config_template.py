from winston_shared.auth_dataclass import Config
from dotenv import load_dotenv
import os

load_dotenv()

twitch = Config(
    name="twitch",
    client_id=os.getenv("TWITCH_CLIENT_ID"),
    client_secret=os.getenv("TWITCH_SECRET"),
    auth_uri="https://id.twitch.tv/oauth2/authorize",
    token_uri="https://id.twitch.tv/oauth2/token",
    scopes=['ADD_SCOPES_HERE'],
    token_file="twitch_token.json",
    redirect_uri=os.getenv("TWITCH_REDIRECT"),
    content_type={'Content-Type': "application/x-www-form-urlencoded"}
)

spotify = Config(
    name="spotify",
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_SECRET"),
    auth_uri="https://accounts.spotify.com/authorize",
    token_uri="https://accounts.spotify.com/api/token",
    scopes=['ADD_SCOPES_HERE'],
    token_file="spotify_token.json",
    redirect_uri=os.getenv("SPOTIFY_REDIRECT"),
    content_type={"Content-Type": "application/x-www-form-urlencoded"}
)