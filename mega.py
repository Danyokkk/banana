import requests

TOKEN = "YOUR_BOT_TOKEN"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": "@daqxn",   # only works if it's a public username and bot has permission
        "text": text
    }
    response = requests.post(url, data=payload)
    return response.json()

send_message("Hello 🚀 This is your bot talking.")
