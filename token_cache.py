import redis

r = redis.Redis(host='localhost', port=6379)

def append_token(token: str):
    r.lpush("refreshTokens", token)

def remove_token(token: str):
    r.lrem("refreshTokens", 0, token)

def token_exists(token):
    tokens = r.lrange("refreshTokens", 0, -1)
    tokens = [t.decode('utf-8') for t in tokens]
    
    return token in tokens