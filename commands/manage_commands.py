def start_battle_controller(update):
    return 'with the update - {}'.format(update)

def commands_init(update, command):
    switcher = {
        "/start-new-battle": start_battle_controller(update),
        "/stop-battle": "u selected stop new battle",
    }
    return switcher.get(command, "Incorrect selection")