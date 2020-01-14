from hashlib import blake2b
from secrets import token_hex


def hash_password(password):
    salt = token_hex(32).encode()
    encoded_pw = password.encode()
    hashed_pw = blake2b(encoded_pw + salt).hexdigest()
    return hashed_pw


hash = hash_password("password")
hash2 = hash_password("password")

print(hash)
