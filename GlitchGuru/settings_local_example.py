"""
This example module illustrates the structure of a local settings file for your Django project. It serves as a template

For security, consider randomly generating the `SECRET_KEY` instead of fixing a static value. Using a random key enhances
security by making it harder to predict. In a production environment, always use a securely generated random key.
"""
import os

SECRET_KEY = '<YOUR VERY SECRET KEY>'

import random
import string

def generate_secret_key():
    """
    Generate a secret key for the Django project.

    :return: The randomly generated secret key.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(50))

# SECRET_KEY = generate_secret_key()

DEBUG = False
ALLOWED_HOSTS = ['<YOUR HOSTS>']

os.environ["PROJECT_DIR"] = "<YOUR PROJECT DIRECTORY>"
os.environ["VENV_DIR"] = "<YOUR VIRTUAL ENVIRONMENT DIRECTORY>"
