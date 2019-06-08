from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from utils import fetch_reply
import os

app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    if True:
        """Respond to incoming calls with a simple text message."""
    # Fetch the message
        print(request.form)
        msg = request.form.get('Body')
        print(msg)
        print("####################################")
        if str(msg).lower() == 'ok' or str(msg).lower() == 'okay':
            print(msg)
            resp = MessagingResponse()
            resp.message('😃')
            print(resp)
            return str(resp)
        print(type(msg))
        sender = request.form.get('From')
        nummedia = request.form.get('NumMedia')
        if(nummedia=='0'):
        # Create reply
            resp = MessagingResponse()
            # print(resp)
            # print(resp.message(fetch_reply(msg, sender )))
            print(type(resp))
            resp_str=fetch_reply(msg,sender)
            #print('reply fetched')

            if len(resp_str[1])!=0:
                resp.message(resp_str[0]).media(resp_str[1])
                print(resp)
            else:
                resp.message(resp_str[0])

            return str(resp)
        else:
            resp = MessagingResponse()
            resp.message('''Thanks for sending me Media
but currently i don't support Media recognition
will update you about this in future''')
            return str(resp)


if __name__ == "__main__":
    print('app started')
    app.run(debug=True)