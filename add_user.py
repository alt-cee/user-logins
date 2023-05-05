import getpass
import hashlib
import sqlite3
import yaml

if __name__ == "__main__":
    with open("db_config.yaml", "r") as file:
        config = yaml.safe_load(file)
        db_path = config[0]["db_path"]

    db_connection = sqlite3.connect(db_path)
    cursor = db_connection.cursor()

    valid_username = False
    while not valid_username:
        username = input("Enter a username: ")
        result = cursor.execute(f"SELECT username FROM users WHERE username = '{username}'")
        existing_users = result.fetchall()
        if len(existing_users) == 0:
            valid_username = True
        else:
            print("Not a valid username.")
    
    password = getpass.getpass("Enter a password: ")
    password_hash = hashlib.sha256(bytearray(password, "utf-8")).hexdigest()

    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{password_hash}');")
    db_connection.commit()
