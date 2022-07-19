import switchbot
import gpiocallback

class EmergencyStop():
    def __init__(self, input_pin, token, deviceID):
        self.plug = switchbot.SmartPlug(token, deviceID)

        gpiocallback.CallbackGPIO(input_pin, self.poweroff)

    def poweroff(self, gpio_no):
        self.plug.turnOff()