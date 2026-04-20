from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ENV VARIABLES
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def home():
    return "Bot Running"

@app.route('/postback')
def postback():
    user_id = request.args.get('user_id')
    amount = request.args.get('amount', '0')

    # MESSAGE FORMAT
    text = f"{user_id}:IN\n{user_id}:IN:{amount}"

    # TELEGRAM SEND
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    requests.get(url, params={
        "chat_id": CHAT_ID,
        "text": text
    })

    return "OK"

# RUN APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
