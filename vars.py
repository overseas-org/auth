import os

SECRET_KEY = os.getenv('SECRET_KEY')
REFRESH_KEY = os.getenv('REFRESH_KEY')
PRIVATE_KEY_PATH = f"{os.getenv('SECRET_KEYS_PATH')}/private.pem"
PUBLIC_KEY_PATH = f"{os.getenv('SECRET_KEYS_PATH')}/public.pem"


with open(PRIVATE_KEY_PATH, "rb") as f:
    PRIVATE_KEY = f.read()

with open(PUBLIC_KEY_PATH, "rb") as f:
    PUBLIC_KEY = f.read()

