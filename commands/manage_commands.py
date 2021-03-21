from templates.welcome import welcome_msg
from controllers.start_new_battle_controller import start_new_battle_controller
from controllers.stop_current_battle_controller import stop_current_battle_controller
from controllers.register_controller import register_controller
from controllers.unregister_controller import unregister_controller

def commands_init(update, command):
    switcher = {
        "/register": register_controller,
        "/unregister": unregister_controller,
        "/start-new-battle": start_new_battle_controller,
        "/stop-current-battle": stop_current_battle_controller,
        "/help-english-battle": welcome_msg,
    }
    strategyCommand = switcher.get(command, welcome_msg)
    return strategyCommand(update)