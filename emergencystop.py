import gpiocallback
import relay

class EmergencyStop():
    def __init__(self, input_pin, relay_pin):
        self.rly = relay.Relay(relay_pin)

        gpiocallback.CallbackGPIO(input_pin, self.poweroff)

    def poweroff(self, gpio_no):
        self.rly.poweroff()
