import secrets
import string

# Generates a randomized state string
def random_string_generator():
    alphabet = string.ascii_letters + string.digits
    state_string = ''.join(secrets.choice(alphabet) for i in range(33))
    return state_string

