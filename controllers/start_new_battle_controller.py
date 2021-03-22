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
            return start_new_battle_template(update, existBattle)

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

        return start_new_battle_template(update, existBattle)
    # TODO make a template for this case
    if existUser is None:
        return """
<b>-----------------------------------------------------------------</b>
<i>just type /accept-battle to play against <u>{PLAYER_ONE}</u></i>
<b>-----------------------------------------------------------------</b>
<i>just type /stop-current-battle to cancel this battle</i>
""".format(PLAYER_ONE=update.message.from_user.username)
    else:
        return """
<b>-----------------------------------------------------------------</b>
<i>just type /accept-battle to play against <u>{PLAYER_ONE}</u></i>
<b>-----------------------------------------------------------------</b>
<i>just type /stop-current-battle to cancel this battle</i>
""".format(PLAYER_ONE=update.message.from_user.username)