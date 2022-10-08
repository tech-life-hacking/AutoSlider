import autoslider
import subscriber

if __name__ == '__main__':
    # slider initialize
    PORTNAME = "YOURMOTORPORTNAME"
    MICROSWITCH_PIN_CLOSE_TO_MOTOR = 19
    MICROSWITCH_PIN_FAR_FROM_MOTOR = 7
    RELAY_PIN = 12

    sld = autoslider.AutoSlider(PORTNAME, MICROSWITCH_PIN_CLOSE_TO_MOTOR, MICROSWITCH_PIN_FAR_FROM_MOTOR, RELAY_PIN)

    # initialize socket
    IPADDRESS = "IPADDRESS"
    PORT = 50101
    sub = subscriber.Subscriber(IPADDRESS, PORT)

    while True:
        event = sub.subscribe()
        sld.run(event)

