import hashlib
import yaml

with open('config.yaml', 'r') as file:
    credentials_list = yaml.safe_load(file)
    credentials = {pair["username"]: pair["password_hash"] for pair in credentials_list}


def is_valid_credentials(username, password):
    if (username in credentials
        and credentials[username] == hashlib.sha256(bytearray(password, "utf-8")).hexdigest()):
        return True
    else:
        return False


if __name__=="__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(is_valid_credentials(username, password))