import hashlib
import sqlite3


if __name__ == "__main__":
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    password_hash = hashlib.sha256(bytearray(password, "utf-8")).hexdigest()

    db_connection = sqlite3.connect("ppab6.db")
    cursor = db_connection.cursor()
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{password_hash}');")
    db_connection.commit()
