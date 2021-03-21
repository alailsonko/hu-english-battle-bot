from setup_app.app_init import mongo
from templates.start_new_battle_template import start_new_battle_template

def start_new_battle_controller(update):
    existUser = mongo.db.users.find_one({
        'username': "{}".format(update.message.from_user.username),
        'chat_id': "{}".format(update.message.chat.id)
        })
    existBattle = mongo.db.battles.find_one({
        'group_id': "{}".format(update.message.chat.id),
    })
    if existUser is not None and existBattle is not None:
        if existBattle['battle_status'] == 'waiting':
            return start_new_battle_template(update)

        if existBattle['battle_status'] == 'started':
            return 'battle already started - you are currently playing with someone'
        result = mongo.db.battles.update_one(
            #find
            {'_id': existBattle['_id']}, 
            #update
            {"$set": { 
                'battle_status': 'waiting',
                'player_one': "{}".format(update.message.from_user.username)
                }
            })

        return start_new_battle_template(update)
    else:
        return 'not found'