from setup_app.app_init import (bot, mongo)
from flask import jsonify
import telegram
from bson.json_util import loads, dumps

def question_controller(update):
    existBattle = mongo.db.battles.find_one({
        'group_id': "{}".format(update.message.chat.id),
    })
    if existBattle is not None:
        if existBattle['battle_status'] == 'started':
            print('helllo')
            questions = mongo.db.questions.find()
            
            print('questions')
            questions = dumps([loads(question) for question in questions])
            print(questions)
            print('questions')
            main_menu_keyboard = [
                [telegram.KeyboardButton('/q - 1 - wrong')],
                [telegram.KeyboardButton('/q - 2 - correct')],
                [telegram.KeyboardButton('/q - 3 - wrong')],
                [telegram.KeyboardButton('/q - 4 - wrong')],
            ]
            reply_kb_markup = telegram.ReplyKeyboardMarkup(
                main_menu_keyboard,
                resize_keyboard=True,
                one_time_keyboard=True)
            
            bot.sendMessage(
                    chat_id=update.message.chat.id, 
                    text='<b>2</b>', 
                    parse_mode='HTML',
                    # reply_to_message_id=msg_id,
                    reply_markup=reply_kb_markup
            )
            
            return '{} - turn'.format(update.message.from_user.username)
        # TODO make a template for this case
        if existBattle['battle_status'] == 'waiting':
            return 'waiting for player two'
        # TODO make a template for this case
        if existBattle['battle_status'] == 'stopped':
            return 'start a new battle'    
