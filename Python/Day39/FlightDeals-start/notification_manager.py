from twilio.rest import Client

TWILIO_SID = YOUR TWILIO SID
TWILIO_AUTH_TOKEN = 
TWILIO_VIRTUAL_NUMBER = 
TWILIO_VERIFIED_NUMBER = 

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, body):
        message = self.client.messages.create(
            body=body,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
