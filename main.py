import getpass
import hashlib
import sqlite3
import yaml


with open("db_config.yaml", "r") as file:
    config = yaml.safe_load(file)
    db_path = config[0]["db_path"]

def is_valid_credentials(username, password):
    db_connection = sqlite3.connect(db_path)
    cursor = db_connection.cursor()

    password_hash = hashlib.sha256(bytearray(password, "utf-8")).hexdigest()
    result = cursor.execute(f"""
        SELECT 
        username,
        password_hash
        FROM 
        users 
        WHERE
        username = '{username}'
        AND
        password_hash = '{password_hash}'""").fetchone()
    
    return result is not None


if __name__=="__main__":
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    if is_valid_credentials(username, password):
        print("Welcome, please enter!")
    else:
        print("Scram!")