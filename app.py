from flask import (Flask, request)
from mastermind.response import get_response
import telegram
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = os.getenv('APP_URL')

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)



@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
  
    # Telegram understands UTF-8, so encode text for unicode compatibility
    print(update)
    if(update.message and update.message.text and update.message.chat.id and update.message.message_id):
        print('reaching')
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        text = update.message.text.encode('utf-8').decode()
        print("got text message :", text)
        
        
        if text[0] == '/':
            response = get_response(text)
            bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)
    else:
        print('no message so far... still listening...')
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def home():
    print(bot.get_me())
    return 'hello'


if __name__ == '__main__':
    app.run(threaded=True)
