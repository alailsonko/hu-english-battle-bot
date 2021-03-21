from templates.welcome import welcome_msg
from controllers.start_new_battle_controller import start_new_battle_controller
from controllers.register_controller import register_controller
from controllers.unregister_controller import unregister_controller

def commands_init(update, command):
    switcher = {
        "/register": register_controller(update),
        "/unregister": unregister_controller(update),
        "/start-new-battle": start_new_battle_controller(update),
        "/help-english-battle": welcome_msg(),
    }
    return switcher.get(command, "Incorrect selection")