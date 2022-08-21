import Jetson.GPIO as GPIO

class CallbackGPIO():
    def __init__(self, input_pin, fn):
        self.gpio = GPIO
        self.input_pin = input_pin

        # Pin Setup:
        self.gpio.setmode(self.gpio.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
        self.gpio.setup(self.input_pin, self.gpio.IN)  # set pin as an input pin
        self.gpio.add_event_detect(self.input_pin, self.gpio.RISING)
        self.gpio.add_event_callback(self.input_pin, callback=fn)

    def cleanup(self):
        self.gpio.cleanup(self.input_pin)