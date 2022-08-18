import Jetson.GPIO as GPIO

class Relay():
    def __init__(self, relay_pin):
        self.gpio = GPIO
        self.relay_pin = relay_pin
        # Pin Setup:
        self.gpio.setmode(self.gpio.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
        self.gpio.setup(self.relay_pin, self.gpio.OUT, initial=self.gpio.HIGH)  # set pin as an input pin

    def poweroff(self):
        self.gpio.output(self.relay_pin, self.gpio.LOW)
