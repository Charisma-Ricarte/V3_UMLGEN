class TrafficLight:
    def __init__(self):
        self.state = "Red"

    def change_to_green(self):
        self.state = "Green"
        print("State changed to Green")

    def change_to_yellow(self):
        self.state = "Yellow"
        print("State changed to Yellow")

    def change_to_red(self):
        self.state = "Red"
        print("State changed to Red")

light = TrafficLight()
light.change_to_green()
light.change_to_yellow()
light.change_to_red()
