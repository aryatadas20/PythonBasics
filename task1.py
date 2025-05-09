users = []

def create_user(user_id, name, email):
    user = {"id": user_id, "name": name, "email": email}
    users.append(user)
    print(f"User {name} created.")


def read_users():
    if not users:
        print("No users available.")
    for user in users:
        print(user)

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print(f"User {user_id} updated.")
            return
    print("User not found.")


def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    print(f"User {user_id} deleted.")

create_user(1, "Alice", "alice@example.com")
create_user(2, "Bob", "bob@example.com")
read_users()
update_user(1, name="Alicia")
delete_user(2)
read_users()