import emergencystop
import threading
import queue
import sliderstate

def slidermotor(q, state):
    while True:
        event = q.get()
        state.change_state(event)
        state.operate()

if __name__ == '__main__':
    state = sliderstate.Context()
    q = queue.Queue()

    token = 'TOKEN'
    deviceID = 'DEVICEID'

    input_pin = PINNUMBER
    btn = sliderstate.getEvent(input_pin, q)

    input_pin = PINNUMBER
    emcbtn = emergencystop.EmergencyStop(input_pin, token, deviceID)

    th = threading.Thread(target=slidermotor, args=(q, state, ))
    th.start()


