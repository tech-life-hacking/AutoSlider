import slider_initializer
import slider_state

class AutoSlider():
    def __init__(self, portname, microswitch_pin_close_to_motor, microswitch_pin_far_from_motor, relay_pin):
        # slider initialize
        self.sld_ini = slider_initializer.SliderInitilizer(portname, microswitch_pin_close_to_motor, microswitch_pin_far_from_motor, relay_pin)

        # slider state initialize
        self.sld_state = slider_state.Context(portname)

        # initialize slider
        self.sld_ini.initialize()

    def run(self, event):
        self.sld_state.change_state(event)
        self.sld_state.operate()