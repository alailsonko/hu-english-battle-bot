from flask import request
from setup_app.app_init import (app, mongo) 
from commands.manage_commands import commands_init
from templates.welcome import welcome_msg
from settings import TOKEN, URL
import telegram

bot = telegram.Bot(token=TOKEN)

@app.route('/{}'.format(TOKEN), methods=['POST', 'GET'])
def respond():
    requestJSON = request.get_json(force=True)
    # retrieve the message in JSON and then transform it to Telegram object
    if requestJSON['update_id']:
        update = telegram.Update.de_json(requestJSON, bot)
    # Telegram understands UTF-8, so encode text for unicode compatibility
    # print(update)
        if update.message:
            if update.message.text and update.message.chat.id and update.message.message_id:
                chat_id = update.message.chat.id
                msg_id = update.message.message_id
                option = update.message.text.encode('utf-8').decode()

                print("got text message :", option)
        
                if option[0] == '/':
                    response = commands_init(update, option)
                    bot.sendMessage(chat_id=chat_id, text=response, parse_mode='HTML',reply_to_message_id=msg_id)
                else:
                    print('does not start with /.')

            if update.message.new_chat_members is not None and len(update.message.new_chat_members) != 0: 

                chat_id = update.message.chat.id

                for members in update.message.new_chat_members:
                    if members.username == 'HUEnglishBattle_bot':
                        print(update)
                        existGroup = mongo.db.battles.find_one({ 'group_id': chat_id})
                        if existGroup is None:
                            mongo.db.battles.insert_one({
                                'group_id': chat_id,
                                'group_type': update.message.chat.type,
                                'group_title': update.message.chat.title,
                                'battle_status': "stopped",
                                'question_status': "5",
                                'player_one': "None",
                                'player_two': "None",
                            })
                        bot.sendMessage(chat_id=chat_id, text=welcome_msg(update), parse_mode='HTML')
                        print('breaking loop...')

                        break

            else:
                print(update)
                print('no message so far... still listening...')

        return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    print('reaching here')

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
