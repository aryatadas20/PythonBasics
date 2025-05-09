import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    if username in users:
        print("Username already exists.")
    else:
        users[username] = hash_password(password)
        print("User registered successfully.")


def login(username, password):
    hashed = hash_password(password)
    if users.get(username) == hashed:
        print("Login successful!")
    else:
        print("Invalid username or password.")

register("alice", "securepass123")
register("bob", "mypassword")

login("alice", "securepass123")  
login("bob", "wrongpass")      
login("charlie", "nopass")      