import requests

class Switchbot():
    def __init__(self, token):
        self.headers = {
            'Authorization': token,
            'Content-Type': 'application/json; charset=utf8',
        }

class SmartPlug():
    def __init__(self, token, deviceID):
        self.switchbot = Switchbot(token)
        self.deviceID = deviceID
        self.turnOff_data = {
            'command': 'turnOff',
            'parameter': 'default',
            'commandType': 'command',
        }

    def turnOff(self):
        response = requests.post('https://api.switch-bot.com/v1.0/devices/' + self.deviceID + '/commands', headers=self.switchbot.headers, json=self.turnOff_data)
