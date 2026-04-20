from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("8704983034:AAEGPn9P-YKIOxuVGiNAw_M0zisU9yh9fT8")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def home():
    return "Bot Running"

@app.route('/postback')
def postback():
    user_id = request.args.get('user_id')
    amount = request.args.get('amount', '0')

    text = f"{user_id}:IN\n{user_id}:IN:{amount}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
