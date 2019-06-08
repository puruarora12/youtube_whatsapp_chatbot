from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from utils import fetch_reply
import os
from random import randint

app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    try:
        """Respond to incoming calls with a simple text message."""
    # Fetch the message
        print(request.form)
        msg = request.form.get('Body')
        sender = request.form.get('From')
        nummedia = request.form.get('NumMedia')
        print(msg)
        print(nummedia)
        print("####################################")
        s= ["I don't support this type of media yet" ,"Thanks for sending me Media but currently i don't support Media recognition will update you about this in future", "Media support isn't a feature yet" , "This Feature will be coming soon" , " Don't push so much pressure on me , I am just a newly born bot" ]
        if (int(nummedia) == 0):

            # Create reply
            resp = MessagingResponse()
            # print(resp)
            # print(resp.message(fetch_reply(msg, sender )))
            if msg ==' ':
                print('from empty body')
                resp.message(s[randint(0 ,len(s)-1)])
                return str(resp)
            elif str(msg).lower() == 'ok' or str(msg).lower() == 'okay':

                print('in the emoji')

                resp.message('😃')
                print(resp)
                return str(resp)
            else:
                pass

            resp_str = fetch_reply(msg, sender)
            # print('reply fetched')

            if len(resp_str[1]) != 0:
                resp.message(resp_str[0]).media(resp_str[1])
                print(resp)
            else:
                resp.message(resp_str[0])

            return str(resp)
        else:
            print('from else')
            resp = MessagingResponse()
            resp.message(s[randint(0 , len(s)-1)])
            return str(resp)

        print(type(msg))



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
    except Exception:
        print('error here\n'+Exception)


if __name__ == "__main__":
    print('app started')
    app.run(debug=True)