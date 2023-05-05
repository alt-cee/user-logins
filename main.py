import hashlib

def is_valid_credentials(username, password):
    credentials = {
        "robert": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
        "anoosh": "3c32608fd9ffd87ae17dbb3a65a509cc8ba5aa395147c99ed20bdba9c434d8c2"
    }
    if (username in credentials
        and credentials[username] == hashlib.sha256(bytearray(password, "utf-8")).hexdigest()):
        return True
    else:
        return False


if __name__=="__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(is_valid_credentials(username, password))