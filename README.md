# flask_server

OAuth authentication server for the Winston Twitch bot. When a user needs to authorize Winston to act on their behalf, they visit this server, get redirected through the Twitch or Spotify consent flow, and the server handles the callback exchanging the auth code for access/refresh tokens and saving them to an accessible directory so the bot can use them without requiring the end-user to reauth.

This is a supporting service for Winston_Bot. Its sole job is to make authenticated API access possible for chat moderation and Spotify song queue requests.

The server runs on a Raspberry Pi and is exposed via a Cloudflare tunnel so that OAuth providers can reach the callback endpoints.


## Setup

### Prerequisites

- Python 3.10+
- [`winston_shared`](https://github.com/cheecho92/winston_shared) installed (provides auth utilities and token storage)
- Twitch and Spotify apps registered with redirect URIs pointing to your Cloudflare tunnel domain
- A Cloudflare tunnel pointed at your respective server/port (Server listens on `127.0.0.1:3000` by default.)

### Install

```bash
pip install -r requirements.txt
```

Make sure `winston_shared` is installed

```bash
pip install -e /path/to/winston_shared
```

### Config

Copy `config_template.py` to `config.py` and fill in your credentials as needed.

Run with app.py


## Related

- [`Winston_Bot`](https://github.com/cheecho92/Winston_Bot) — the bot that handles the tokens generated and contains the chat moderation logic
- [`winston_shared`](https://github.com/cheecho92/winston_shared) — shared auth logic and tokens used by both services