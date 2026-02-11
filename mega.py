import requests

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=payload)
    return response.json()

send_message("Hello Danylo 🚀 Your Python script is working!")
