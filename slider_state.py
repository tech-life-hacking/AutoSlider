import slider

class State():
    def operate(self):
        raise NotImplementedError("operate is abstractmethod")

class Open(State):
    def __init__(self, portname):
        self.sld = slider.Slider(portname)

    def operate(self, laststate, state):
        if laststate != state:
            self.sld.pull()

class Close(State):
    def __init__(self, portname):
        self.sld = slider.Slider(portname)

    def operate(self, laststate, state):
        if laststate != state:
            self.sld.push()

class Context:
    def __init__(self, portname):
        self.open = Open(portname)
        self.close = Close(portname)
        self.state = self.close
        self.laststate = self.state

    def change_state(self, event):
        self.laststate = self.state
        if event == "pull":
            self.state = self.open
        elif event == "push":
            self.state = self.close
        else:
            pass

    def operate(self):
        self.state.operate(self.laststate, self.state)

