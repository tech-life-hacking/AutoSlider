import gpiocallback
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'DDT_M0601C_111'))
import DDT_M0601C_111.motor as motor

class State():
    def operate(self):
        raise NotImplementedError("operate is abstractmethod")

class Open(State):
    def __init__(self):
        port_name = "PORTNAME"
        self.motor = motor.Motor(port_name, 1)

    def operate(self):
        self.motor.rotate(200, 10)
        self.motor.stop()

class Close(State):
    def __init__(self):
        port_name = "PORTNAME"
        self.motor = motor.Motor(port_name, 1)

    def operate(self):
        self.motor.rotate(-200, 10)
        self.motor.stop()

class Context:
    def __init__(self):
        self.open = Open()
        self.close = Close()
        self.state = self.close

    def change_state(self, hand):
        if hand == "Open":
            self.state = self.open
        elif hand == "Close":
            self.state = self.close
        else:
            pass

    def operate(self):
        self.state.operate()

class getEvent():
    def __init__(self, input_pin, q):
        self.laststate = "Close"
        self.q = q

        gpiocallback.CallbackGPIO(input_pin, self.getevent)

    def getevent(self, gpio_no):
        if self.laststate == "Open":
            state = "Close"
        else:
            state = "Open"
        self.laststate = state
        self.q.put(state)
