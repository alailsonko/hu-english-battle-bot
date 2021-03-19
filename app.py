from flask import (Flask, request)
from mastermind.response import get_response
import telegram

TOKEN = '1606387832:AAFtuOGfvPw-8ah0F8MWWPB802oLy0MrJzE'

URL = "https://hu-english-battle-bot.herokuapp.com/"

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/1606387832:AAFtuOGfvPw-8ah0F8MWWPB802oLy0MrJzE'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

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
