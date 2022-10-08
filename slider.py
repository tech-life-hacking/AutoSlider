import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'DDT_M0601C_111'))
import DDT_M0601C_111.usart as usart
import time

class Slider():
    def __init__(self, port_name):
        self.port_name = port_name
        self.cp = usart.CommunicationProtocol(self.port_name)

    def push(self):
        Speed, Mode, ID, Acce, Brake_P = 200, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)
        time.sleep(2)
        Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)

    def pull(self):
        Speed, Mode, ID, Acce, Brake_P = -200, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)
        time.sleep(2)
        Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)

    def stop(self):
        Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)
