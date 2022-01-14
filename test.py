
from time import sleep
import json
import config
from flask import Flask, Response, render_template
import time

app = Flask(__name__)
quit = False
SETTINGS = config.get_config()
RECENTS_FOLDER = '/media/{}/config/'.format(SETTINGS['core_storage'])

details = {}

@app.route('/')
def index():
    return render_template('details.html')


@app.route('/details')
def game_details():
    def get_game_details():
        while True:
            json_data = json.dumps(
                {'rom_id': 5815, 'system_id': 20, 'name': '007: Everything or Nothing', 'region': 'Europe', 'front_cover': 'https://gamefaqs.gamespot.com/a/box/5/0/6/53506_front.jpg', 'back_cover': 'https://gamefaqs.gamespot.com/a/box/5/0/6/53506_back.jpg', 'description': "Think like Bond, act like Bond, and experience an entirely new Bond adventure.James Bond, the world's greatest secret agent, returns in Everything or Nothing with new guns and gadgets, combat skills, and clever tricks--and it's up to you to put them to good use.Travel through four exciting continents including the Valley of the Kings in Egypt and the French Quarter in New Orleans.The game also features two-player co-op missions and four-player multiplayer arena modes.", 'developer': 'Griptonite Games', 'publisher': None, 'genre': 'Action,Shooter,Third-Person,Modern', 'release_date': 'Nov 17, 2003', 'gamefaqs': 'http://www.gamefaqs.com/gba/914854-007-everything-or-nothing'})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(get_game_details(), mimetype='text/event-stream')



app.run(threaded=True,host='0.0.0.0', port=8080)

