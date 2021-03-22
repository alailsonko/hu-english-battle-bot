from setup_app.app_init import bot
import telegram

def question_controller(update):
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