import os

import flask
import openai

from process import Message

app = flask.Flask(__name__)
request = flask.request

PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
ACCESS_TOKEN = os.getenv("WHATSAPP_API_KEY")
AUTH_PHONE_NUMBER = os.getenv("AUTHORIZED_PHONE_NUMBER")
WHATSAPP_VERIFY_TOKEN  = os.getenv("WHATSAPP_VERIFY_TOKEN")

msg = Message(ACCESS_TOKEN, PHONE_NUMBER_ID)

openai.api_key = os.getenv("OPENAI_API_KEY")


def auth(meth: str = "POST") -> bool:
    if meth == "POST":
        verify_token = request.get_json()["hub.verify_token"]
    elif meth == "GET":
        verify_token = request.args.get("hub.verify_token")
    return verify_token == WHATSAPP_VERIFY_TOKEN


def authorized_phone_number(phone_number: str) -> bool:
    if phone_number == AUTH_PHONE_NUMBER:
        return True
    else:
        msg.send_message(phone_number, "You are not authorized to use this bot.")
        return False


@app.get("/")
def index():
    return "Hello WA"


@app.get("/webhook")
def webhook():
    if auth():
        return request.args.get("hub.challenge")
    else:
        flask.abort(403)


@app.post("/webhook")
def process_message():
    data = request.get_json()
    print(request.args)
    try:
        for entry in data["entry"]:
            for change in entry["changes"]:
                field = change["field"]
                match field:
                    case "messages":
                        messages = change["value"]["messages"]
                        for message in messages:
                            fromPhoneNumber = message["from"]
                            if authorized_phone_number(fromPhoneNumber):
                                match message["type"]:
                                    case "text":
                                        prompt = message["text"]["body"]
                                        # if prompt conatins /image
                                        # then send image
                                        if prompt[:6] == "/image":
                                            res = openai.Image.create(
                                                prompt=prompt[7:],
                                                n=2,
                                            )
                                            for image in res["data"]:
                                                msg.send_image_url(
                                                    fromPhoneNumber, image["url"]
                                                )
                                            break
                                        else:
                                            res = openai.Completion.create(
                                                engine="text-davinci-003",
                                                prompt=prompt,
                                                max_tokens=500,
                                            )
                                            output = ""
                                            for choice in res["choices"]:
                                                output += choice["text"].strip()
                                            msg.send_message(fromPhoneNumber, output)
                                        break
                        break
    except Exception as e:
        print(e)
    return "OK"
