import DDT_M0601C_111.usart as usart
import slider

class State():
    def operate(self):
        raise NotImplementedError("operate is abstractmethod")


class NoDetected(State):
    def __init__(self, port_name):
        self.cp = usart.CommunicationProtocol(port_name)

    def operate(self, state, laststate, sld):
        if sld.getlastposition() != sld.getposition():
            Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
            self.cp.Control_Motor(Speed, ID, Acce, Brake_P)

class PAPER(State):
    def __init__(self, port_name):
        self.cp = usart.CommunicationProtocol(port_name)

    def operate(self, state, laststate, sld):
        if laststate != state:
            Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
            self.cp.Control_Motor(Speed, ID, Acce, Brake_P)

class SCISSORS(State):
    def __init__(self, port_name):
        self.cp = usart.CommunicationProtocol(port_name)

    def operate(self, state, laststate, sld):
        if sld.getposition() < 75:
            if laststate != state:
                Speed, Mode, ID, Acce, Brake_P = -200, 2, 1, 0, 0
                self.cp.Control_Motor(Speed, ID, Acce, Brake_P)
            sld.countup()
        else:
            if sld.getlastposition() != sld.getposition():
                Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
                self.cp.Control_Motor(Speed, ID, Acce, Brake_P)


class FINGER(State):
    def operate(self, state, laststate):
        pass


class STONE(State):
    def __init__(self, port_name):
        self.cp = usart.CommunicationProtocol(port_name)

    def operate(self, state, laststate, sld):
        if sld.getposition() > 0:
            if laststate != state:
                Speed, Mode, ID, Acce, Brake_P = 200, 2, 1, 0, 0
                self.cp.Control_Motor(Speed, ID, Acce, Brake_P)
            sld.countdown()
        else:
            if sld.getlastposition() != sld.getposition():
                Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
                self.cp.Control_Motor(Speed, ID, Acce, Brake_P)


class Context:
    def __init__(self, port_name, sld):
        self.nodetected = NoDetected(port_name)
        self.paper = PAPER(port_name)
        self.scissors = SCISSORS(port_name)
        self.finger = FINGER()
        self.stone = STONE(port_name)
        self.state = self.nodetected
        self.laststate = self.nodetected

    def change_state(self, hand):
        self.laststate = self.state
        if hand == "NoDetected":
            self.state = self.nodetected
        elif hand == "PAPER":
            self.state = self.paper
        elif hand == "SCISSORS":
            self.state = self.scissors
        elif hand == "FINGER":
            self.state = self.finger
        elif hand == "STONE":
            self.state = self.stone
        else:
            # raise ValueError("change_state method must be in {}".format(
            #     ["nodetected", "paper", "scissors", "stone"]))
            pass

    def getstate(self):
        return self.state

    def getlaststate(self):
        return self.laststate

    def operate(self, sld):
        self.state.operate(self.state, self.laststate, sld)
