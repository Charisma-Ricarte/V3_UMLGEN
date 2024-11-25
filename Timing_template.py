class Sensor:
    def __init__(self):
        self.value = 0

    def update_value(self, new_value):
        self.value = new_value
        print(f"Sensor value updated to {self.value}")

class Display:
    def show_value(self, value):
        print(f"Displaying value: {value}")

sensor = Sensor()
display = Display()

sensor.update_value(10)
display.show_value(sensor.value)

sensor.update_value(20)
display.show_value(sensor.value)
