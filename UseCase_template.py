class User:
    def login(self, username, password):
        print("Logging in...")

class Admin(User):
    def delete_user(self, user_id):
        print(f"Deleting user {user_id}")

# Actions
user = User()
user.login("john_doe", "password123")
admin = Admin()
admin.delete_user(42)
