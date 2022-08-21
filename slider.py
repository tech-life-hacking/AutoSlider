import DDT_M0601C_111.usart as usart
import gpiocallback
import time

class Slider():
    def __init__(self, port_name, input_pin, q):
        self.cp = usart.CommunicationProtocol(port_name)

        self.q = q

        self.gpio = gpiocallback.CallbackGPIO(input_pin, self.findedge)

    def findedge(self, gpio_no):
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
        self.q.put("initializing finished")

    def approachedge(self):
        Speed, Mode, ID, Acce, Brake_P = 10, 2, 1, 0, 0
        self.cp.Control_Motor(Speed, ID, Acce, Brake_P)


    def countup(self):
        self.lastx = self.x
        self.x += 1

    def countdown(self):
        self.lastx = self.x
        self.x += -1

    def getposition(self):
        return self.x

    def getlastposition(self):
        return self.lastx
