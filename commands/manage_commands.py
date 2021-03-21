from templates.welcome import welcome_msg
from controllers.start_battle_controller import start_battle_controller

def commands_init(update, command):
    switcher = {
        "/start-new-battle": start_battle_controller(update),
        "/help-english-battle": welcome_msg(),
    }
    return switcher.get(command, "Incorrect selection")