import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'DDT_M0601C_111'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'HandGestureRecognition'))
import HandGestureRecognition.scripts.video as video
import HandGestureRecognition.scripts.hand as hand
import DDT_M0601C_111.usart as usart
import emergencystop
import queue
import cv2
import gestures
import slider

if __name__ == "__main__":

    # motor setup
    port_name = PORTNAME
    cp = usart.CommunicationProtocol(port_name)

    # setup emergency botton
    input_pin = PINNUMBER
    relay_pin = PINNUMBER
    emcbtn = emergencystop.EmergencyStop(input_pin, relay_pin)

    # initialize
    input_pin = PINNUMBER
    q1 = queue.Queue()
    sld = slider.Slider(port_name, input_pin, q1)

    # approaching an edge of a slider
    sld.approachedge()

    # initializing finished
    event = q1.get()

    input_pin = PINNUMBER
    emcbtn1 = emergencystop.EmergencyStop(input_pin, relay_pin)

    # class of gestures for OAK
    class_names = ['LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE',
                   'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    # model path for OpenCV AI Kit
    model_path = "HandGestureRecognition/model/hands_OAK.tflite"

    # For HandGestureRecognition for OpenCV AI Kit
    myhands = hand.Hand(hand.OAKCamera(class_names, model_path))
    videocap = video.VideoCap(video.OAKCamera())
    ges = gestures.Context(port_name, sld)

    while True:

        frame, hands = videocap.capture()

        try:
            # Recognize gestures
            myhands.run(hands)
            kind_of_hands = myhands.get_gestures()
            ges.change_state(kind_of_hands)
            ges.operate(sld)
            cv2.putText(frame, kind_of_hands,
                        (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
        except IndexError:
            pass

        videocap.show(frame)
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):
            break

    videocap.exit()
