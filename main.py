def is_valid_credentials(username, password):
    if username == "robert" and password == "password123":
        return "You've unlocked the system."
    else:
        return "Scram!"

if __name__=="__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(is_valid_credentials(username, password))