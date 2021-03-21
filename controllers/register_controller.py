from setup_app.app_init import mongo

def register_controller(update):
    existUser = mongo.db.users.find_one({'{}'.format(update.message.from_user.username): "{}".format(update.message.from_user.id)})
    if existUser is None:
        mongo.db.users.insert_one({'{}'.format(update.message.from_user.username): "{}".format(update.message.from_user.id)})
        return '{} - registered successfully'.format(update.message.from_user.username)
    else:
        return '{} - user already exist.'.format(update.message.from_user.username)
