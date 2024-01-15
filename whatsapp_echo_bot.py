from pprint import pprint

import requests
from flask import Flask
from flask import request

app = Flask(__name__)


def send_message(chat_id, text):
    """
    Send message to chat_id.
    :param chat_id: Phone number + "@c.us" suffix - 1231231231@c.us
    :param text: Message for the recipient
    """
    # Send a text back via WhatsApp HTTP API
    response = requests.post(
        "http://localhost:3000/api/sendText",
        json={
            "chatId": chat_id,
            "text": text,
            "session": "default",
        },
    )
    response.raise_for_status()

def reply(chat_id, message_id, text):
    response = requests.post(
        "http://localhost:3000/api/reply",
        json={
            "chatId": chat_id,
            "text": text,
            "reply_to": message_id,
            "session": "default",
        },
    )
    response.raise_for_status()


def send_seen(chat_id, message_id, participant):
    response = requests.post(
        "http://localhost:3000/api/sendSeen",
        json={
            "session": "default",
            "chatId": chat_id,
            "messageId": message_id,
            "participant": participant,
        },
    )
    response.raise_for_status()


@app.route("/")
def whatsapp_echo():
    return "WhatsApp Echo Bot is ready!"

def sendWhatsappText(chatid, msg, session,groupid=""):
    try:
        url = "http://localhost:3000/api/sendText"
        payload = {
            'chatId': chatid,
            'text': msg,
            'session': session
        }
        resp = requests.post(url, json=payload)

        if resp.status_code == 200 or resp.status_code == 201:
            print("Message sent successfully.")
            #print(resp.json())
        else:
            print(f"Error: {resp.status_code}")
            print(resp.text)
 
        if resp.status_code == 200 or resp.status_code == 201:
            print("Start Typing message successfully.")
            #print(resp.json())
        else:
            print(f"Error: {resp.status_code}")
            print(resp.text)

    except Exception as e:
        print(f"Exception in Start Typing: {e}")



def sendStartTyping(chatid, msg, session):
    try:
        url = "http://localhost:3000/api/startTyping"
        payload = {
            'chatId': chatid,
            'text': msg,
            'session': session
        }
        resp = requests.post(url, json=payload)

        if resp.status_code == 200 or resp.status_code == 201:
            print("Start Typing message successfully.")
            #print(resp.json())
        else:
            print(f"Error: {resp.status_code}")
            print(resp.text)

    except Exception as e:
        print(f"Exception in Start Typing: {e}")


def sendStopTyping(chatid, msg, session):
    try:
        url = "http://localhost:3000/api/stopTyping"
        payload = {
            'chatId': chatid,
            'text': msg,
            'session': session
        }
        resp = requests.post(url, json=payload)

        if resp.status_code == 200 or resp.status_code == 201:
            print("Stop Typing message successfully.")
            #print(resp.json())
        else:
            print(f"Error: {resp.status_code}")
            print(resp.text)

    except Exception as e:
        print(f"Exception in Stop Typing: {e}")






@app.route("/bot", methods=["GET", "POST"])
def whatsapp_webhook():
    try:

        if request.method == "GET":
            return "WhatsApp Echo Bot is ready!"

        data = request.get_json()
        pprint(data)
        if data["event"] != "message" and data['event'] != "message.ack":
            print("hhe-22222222222222222222222")
            return f"Unknown event {data['event']}"
    
        payload = data["payload"]
        print(str(payload), "shjshhhh")
        # The text
        text = payload["body"]

        chat_id = payload["from"]
        message_id = payload['id']
        chat_id2 = payload['to']

        participant = payload.get('participant')
        if chat_id2 == "919867530476@c.us":
            send_seen(chat_id=chat_id, message_id=message_id, participant=participant)
            #send_message(chat_id=chat_id, text=text)
            # OR reply on the message
            #reply(chat_id=chat_id, message_id=message_id, text=text)
            ch_id = "918830182271-1576171664@g.us"
            ch_id2 ="120363220852928966@g.us"
            ch_id1= "120363191397732686@g.us"
            sendStartTyping(msg=text,chatid=ch_id,session="default")
            sendStopTyping(msg=text,chatid=ch_id,session="default")
            sendWhatsappText(msg=text,chatid=ch_id,session="default")
            # Send OK back
            return "OK"
        elif chat_id2 == '917065275087@c.us':
            send_seen(chat_id=chat_id, message_id=message_id, participant=participant)
            #send_message(chat_id=chat_id, text=text)
            # OR reply on the message
            #reply(chat_id=chat_id, message_id=message_id, text=text)
            ch_id ="120363220852928966@g.us"
            ch_id1= "120363191397732686@g.us"
            sendStartTyping(msg=text,chatid=ch_id,session="default")
            sendStopTyping(msg=text,chatid=ch_id,session="default")
            sendWhatsappText(msg=text,chatid=ch_id,session="default")
            # Send OK back
            return "OK"
    except Exception as e:
        print(str (e),"ERROR")    






