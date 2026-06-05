import secrets
import string
import requests

# Generates a randomized state string
def random_string_generator():
    alphabet = string.ascii_letters + string.digits
    state_string = ''.join(secrets.choice(alphabet) for i in range(33))
    return state_string

def authenticated_user(access_token, client_id):
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Client-Id': client_id
    }
    req = requests.get("https://api.twitch.tv/helix/users", headers=headers)
    req.raise_for_status()
    response = req.json()
    return response['data'][0]['login']