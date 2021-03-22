from setup_app.app_init import mongo

def accept_battle_controller(update):
    existBattle = mongo.db.battles.find_one({
        'group_id': "{}".format(update.message.chat.id),
    })
    if existBattle is not None:
        if existBattle['battle_status'] == 'waiting':
            if existBattle['player_one'] == "{}".format(update.message.from_user.username):
                return 'u can not battle against yourself, wait for a user.'
            mongo.db.battles.update_one(
                #find
                {'_id': existBattle['_id']}, 
                #update
                {"$set": { 
                    'battle_status': 'started',
                    'player_two': "{}".format(update.message.from_user.username)
                    }
                })
            return '{} - accepted the battle2'.format(update.message.from_user.username)
        if existBattle['battle_status'] == 'started':
            return '{} - accepted the battle'.format(update.message.from_user.username)
        if existBattle['battle_status'] == 'stopped':
            return 'has no battle waiting for a player, start a new one'