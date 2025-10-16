import jwt
from datetime import datetime, timedelta


def create_jwt(user, secret, days=0, hours=0, minutes=0, seconds=0 , symmetric_key=True):
    if symmetric_key:
        algorithm = "HS256"
    else:
        algorithm = "RS256"
    user["exp"] = int((datetime.now() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)).timestamp())
    token = jwt.encode(user, secret, algorithm=algorithm)
    return token

    
def verify_jwt(token, secret, symmetric_key=True):
    if symmetric_key:
        algorithm = "HS256"
    else:
        algorithm = "RS256"
    try:
        decoded_payload = jwt.decode(token, secret, algorithms=[algorithm])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired.")
    except jwt.InvalidTokenError as e:
        raise Exception(f"Invalid token: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")