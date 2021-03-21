from setup_app.app_init import mongo

def register_controller(update):
    existUser = mongo.db.users.find_one({'username': "{}".format(update.message.from_user.username)})
    if existUser is None:
        mongo.db.users.insert_one({
            'username': "{}".format(update.message.from_user.username),
            'chat_id': "{}".format(update.message.chat.id),
            'chat_type': "{}".format(update.message.chat.type),
            'chat_title': "{}".format(update.message.chat.title),
            'score': '0xp'
            })
        return '{} - registered successfully'.format(update.message.from_user.username)
    else:
        return '{} - user already exist.'.format(update.message.from_user.username)
