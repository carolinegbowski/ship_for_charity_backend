FILE = "/home/c/tmp/credentials/ship4charity.txt"


def password(file=FILE):
    with open(FILE) as password:
        return password.read()
