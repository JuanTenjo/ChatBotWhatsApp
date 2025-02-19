from flask import Flask, request
import json
import util
import whatsapp

chat = Flask(__name__)
@chat.route('/Welcome', methods=['GET'])
def index():
    return "Welcome"

#ENVIAR MENSAJES

@chat.route('/WhatsApp', methods=['GET'])
def VerifyToken():

    try:
        accessToken= "82das23dsj323j8"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")   

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400

#RECIBIR MENSAJES
@chat.route('/WhatsApp', methods =['POST'])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]
        
        text = util.GetTextUser(message)
        GenerateMessage(text, number)
        print (text)
        
        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"

def GenerateMessage(text, number):
    text = "El user dijo: " + text
    whatsapp.SendMessageWhastapp(text, number)


if(__name__ == '__main__'):
    chat.run()