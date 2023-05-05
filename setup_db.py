import sqlite3


if __name__ == "__main__":
    db_connection = sqlite3.connect("ppab6.db")
    cursor = db_connection.cursor()

    cursor.execute("CREATE TABLE users(username VARCHAR, password_hash VARCHAR);")


