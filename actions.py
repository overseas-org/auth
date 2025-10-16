from jwt_manage import create_jwt, verify_jwt
from neibhors.account import validate_user, create_user, get_account_by_name, create_account
from vars import PRIVATE_KEY, PUBLIC_KEY ,REFRESH_KEY
from token_cache import append_token, remove_token, token_exists


def login_user(user):
    response = validate_user(user)
    if response.status_code != 200:
        raise Exception(response.text)
    user = response.json()
    return get_tokens(user)

def logout_user(token):
    remove_token(token)

def sinup_user(user):
    new_account = user.pop("create_account")
    sso_verified = False
    if "sso_verified" in user:
        sso_verified = user.pop("sso_verified")
    if new_account:
        account = user.pop("account")
        account_id = create_account(account)
    else:
        # find a way to get approval for adding this user
        account = user.pop("account")
        account_id = get_account_by_name(account)
    user["account_id"] = account_id
    create_user(user)
    if sso_verified:
        user["sso_verified"] = True
    tokens = login_user(user)
    return tokens

def verify_token(token):
    paylod = verify_jwt(token, PUBLIC_KEY, symmetric_key=False)
    return bool(paylod)


def refresh_token(token):
    if not token_exists(token):
        raise Exception("Invalid refresh token")
    user = verify_jwt(token, REFRESH_KEY, symmetric_key=True)
    new_tokens = get_tokens(user)
    remove_token(token)
    return new_tokens
    

def get_tokens(user):
    accessToken = create_jwt(user, PRIVATE_KEY, minutes=15, symmetric_key=False)
    refreshToken = create_jwt(user, REFRESH_KEY, days=1)
    append_token(refreshToken)
    return {
        "accessToken": accessToken,
        "refreshToken": refreshToken
    }