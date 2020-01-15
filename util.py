import bcrypt


def hash_password(password):
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    return password


def check_password(password, password_hash):
    return bcrypt.checkpw(password, password_hash)
