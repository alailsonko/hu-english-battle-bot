from setup_app.app_init import mongo
from templates.stop_current_battle_template import stop_current_battle_template

def stop_current_battle_controller(update):
    existBattle = mongo.db.battles.find_one({
        'group_id': "{}".format(update.message.chat.id),
    })
    if existBattle is not None:
        if existBattle['battle_status'] != 'stopped':
            mongo.db.battles.update_one(
                #find
                {'_id': existBattle['_id']}, 
                #update
                {"$set": { 
                    'battle_status': 'stopped',
                    'player_one': 'None',
                    'player_two': 'None',
                    }
                })
            print('existBattle')
            print(existBattle)
            print('existBattle')
            return stop_current_battle_template(update)
        if existBattle['battle_status'] == 'stopped':
            return stop_current_battle_template(update)
