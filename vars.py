import os

SECRET_KEY = os.getenv('SECRET_KEY')
REFRESH_KEY = os.getenv('REFRESH_KEY')
PRIVATE_KEY_PATH = os.getenv('PRIVATE_KEY_PATH')
PUBLIC_KEY_PATH = os.getenv('PUBLIC_KEY_PATH')

with open(PRIVATE_KEY_PATH, "rb") as f:
    PRIVATE_KEY = f.read()

with open(PUBLIC_KEY_PATH, "rb") as f:
    PUBLIC_KEY = f.read()

