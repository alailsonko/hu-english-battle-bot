def start_new_battle_template(update, existBattle):
    if existBattle is not None:
        return """
            <b>--------LOG_INFO <u>waiting for player_two</u>---------</b>
            <b>    </b>
            <strong>ENGLISH BATTLE STARTED</strong>
            <b>-------------------------------------------</b>
            <strong>{PLAYER_ONE} VS {PLAYER_TWO}</strong>
<b>-----------------------------------------------------------------</b>
<i>just type /accept-battle to play against <u>{PLAYER_ONE}</u></i>
<b>-----------------------------------------------------------------</b>
<i>just type /stop-current-battle to cancel this battle</i>
        """.format(PLAYER_ONE=existBattle['player_one'], PLAYER_TWO='waiting for player two...')
    return """
            <b>--------LOG_INFO <u>waiting for player_two</u>---------</b>
            <b>    </b>
            <strong>ENGLISH BATTLE STARTED</strong>
            <b>-------------------------------------------</b>
            <strong>{PLAYER_ONE} VS {PLAYER_TWO}</strong>
<b>-----------------------------------------------------------------</b>
<i>just type /accept-battle to play against <u>{PLAYER_ONE}</u></i>
<b>-----------------------------------------------------------------</b>
<i>just type /stop-current-battle to cancel this battle</i>
        """.format(PLAYER_ONE=update.message.from_user.username, PLAYER_TWO='waiting for player two...')

# """
# <b>bold</b>, <strong>bold</strong>
# <i>italic</i>, <em>italic</em>
# <u>underline</u>, <ins>underline</ins>
# <s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
# <b>bold <i>italic bold <s>italic bold strikethrough</s> <u>underline italic bold</u></i> bold</b>
# <a href="http://www.example.com/">inline URL</a>
# <a href="tg://user?id=123456789">inline mention of a user</a>
# <code>inline fixed-width code</code>
# <pre>pre-formatted fixed-width code block</pre>
# <pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
#     """



