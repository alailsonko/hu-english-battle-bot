from setup_app.app_init import mongo

def unregister_controller(update):
    findUser = mongo.db.users.find_one({
        'username': "{}".format(update.message.from_user.username)
        'chat_id': "{}".format(update.message.chat.id)
        })
    if findUser is not None:
        mongo.db.users.delete_one({'_id': findUser['_id']})
        return '{} - unregistered successfully'.format(update.message.from_user.username)