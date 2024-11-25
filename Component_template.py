class Database:
    def query(self, sql):
        print(f"Executing query: {sql}")

class Backend:
    def __init__(self):
        self.database = Database()

    def get_data(self):
        self.database.query("SELECT * FROM users")

class Frontend:
    def __init__(self):
        self.backend = Backend()

    def display_data(self):
        self.backend.get_data()

frontend = Frontend()
frontend.display_data()
