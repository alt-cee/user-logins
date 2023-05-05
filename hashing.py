import hashlib

credentials = {
    "robert": "password123",
    "anoosh": "snuffles456"
}

if __name__ == "__main__":
    for username, password in credentials.items():
        b = bytearray(password, 'utf-8')
        print(username, hashlib.sha256(b).hexdigest())
