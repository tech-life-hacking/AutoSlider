import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'DDT_M0601C_111'))
import DDT_M0601C_111.usart as usart
import gpiocallback
import time
import emergencystop
import queue

class SliderInitilizer():
    def __init__(self, port_name, microswitch_pin_close_to_motor, microswitch_pin_far_from_motor, relay_pin):
        self.port_name = port_name
        self.cp = usart.CommunicationProtocol(self.port_name)
        self.microswitch_pin_close_to_motor = microswitch_pin_close_to_motor
        self.microswitch_pin_far_from_motor = microswitch_pin_far_from_motor
        self.relay_pin = relay_pin

        self.initialize_queue = queue.Queue()

    def found_edge(self, gpio_no):
        Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)
        Speed, Mode, ID, Acce, Brake_P = -200, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)
        time.sleep(1)
        Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)

        self.gpio.cleanup()

        self.x = 0
        self.lastx = 0
        self.initialize_queue.put("initializing finished")

    def approach_edge(self):
        Speed, Mode, ID, Acce, Brake_P = 50, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)

    def initialize(self):
        # setup emergency botton
        emergencystop.EmergencyStop(self.microswitch_pin_far_from_motor, self.relay_pin)

        self.gpio = gpiocallback.CallbackGPIO(self.microswitch_pin_close_to_motor, self.found_edge)

        # approaching an edge of a slider
        self.approach_edge()

        # initializing finished
        self.initialize_queue.get()

        # setup emergency botton
        emergencystop.EmergencyStop(self.microswitch_pin_close_to_motor, self.relay_pin)