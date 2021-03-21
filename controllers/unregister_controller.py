from setup_app.app_init import mongo

def unregister_controller(update):
    return '{} - unregistered successfully'.format(update.message.from_user.username)
       