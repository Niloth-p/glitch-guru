import os

SECRET_KEY = '<YOUR VERY SECRET KEY>'

# import random
# import string

# def generate_secret_key():
#     chars = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(chars) for _ in range(50))

# SECRET_KEY = generate_secret_key()

DEBUG = False
ALLOWED_HOSTS = ['<YOUR HOSTS>']

os.environ["PROJECT_DIR"] = "<YOUR PROJECT DIRECTORY>"
os.environ["VENV_DIR"] = "<YOUR VIRTUAL ENVIRONMENT DIRECTORY>"
