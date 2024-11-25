class Server:
    def __init__(self, name):
        self.name = name

    def deploy(self, application):
        print(f"Deploying {application} to {self.name}")

class Application:
    def __init__(self, name):
        self.name = name

    def deploy_to(self, server):
        server.deploy(self.name)

server = Server("Production Server")
app = Application("WebApp")
app.deploy_to(server)
