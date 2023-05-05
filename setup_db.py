import os
import sqlite3

db_filename = "ppab6.db"

if __name__ == "__main__":
    if os.path.isfile(db_filename):
        db_connection = sqlite3.connect(db_filename)
        cursor = db_connection.cursor()
        result = cursor.execute("SELECT COUNT(username) FROM users;")
        n_rows = result.fetchone()[0]
        print(f"Database already exists with {n_rows} rows.")

        delete_db = None
        while delete_db not in ['y', 'n']:
            delete_db = input("Do you want to delete and recreate the database? [y/n]: ")
        
        if delete_db == 'y':
            os.remove(db_filename)
            db_connection = sqlite3.connect(db_filename)
            cursor = db_connection.cursor()
            cursor.execute("CREATE TABLE users (username VARCHAR, password_hash VARCHAR);")
