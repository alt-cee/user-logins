def is_valid_credentials(username, password):
    credentials = {
        "robert": "password123",
        "anoosh": "snuffles456"
    }
    if (username in credentials) and credentials[username] == password:
        return "You've unlocked the system."
    else:
        return "Scram!"


if __name__=="__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(is_valid_credentials(username, password))