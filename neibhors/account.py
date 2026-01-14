import requests
from neibhors.neibhors import account 


def validate_user(user):
    response = requests.post(f"{account}/validate_user", json={ "user": user })
    return response
    # if response.status_code != 200:
    #     False
    # else:
    #     return True

def create_user(user):
    response = requests.post(f"{account}/user", json={"user": user})
    if response.status_code != 200:
        raise Exception(response.text)

def create_account(account_name):
    response = requests.post(f"{account}/account", json={"account": {"name": account_name}})
    if response.status_code != 201:
        raise Exception(response.text)
    else:
        data = response.json()
        return data["objectId"]

def get_account_by_name(account_name):
    response = requests.get(f"{account}/account_by_name", json={"account": account_name})
    if response.status_code != 200:
        raise Exception(response.text)
    else:
        data = response.json()
        return data["id"]
    
def check_if_account_exists(account_name):
    response = requests.get(f"{account}/account_exists", json={"account": account_name})
    return response.text, response.status_code
