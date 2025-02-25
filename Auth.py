import sqlite3
import bcrypt

# Register a new user
def register_user(username, password):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Hash the password
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")

    conn.close()

# Login function
def login_user(username, password):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result and bcrypt.checkpw(password.encode(), result[0]):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Example usage
# register_user("deepak", "balram")
# login_user("deepak", "balram")
