from time import sleep
import json
import config
import mister
import cores
import time
from flask import Flask, request, Response, redirect, send_file, render_template
import openvgdb

app = Flask(__name__)
quit = False
SETTINGS = config.get_config()
maps = cores.read_file_map()
RECENTS_FOLDER = '/media/{}/config/'.format(SETTINGS['core_storage'])

details = {}


@app.route('/')
def index():
    return render_template('details.html')


@app.route('/details')
def game_details():
    def get_game_details():
        while True:
            global details
            core = mister.get_running_core()
            #map_core = cores.get_map(core)
            game,filepath,filename = mister.get_last_game(core)
            if game != "":  
                hash = mister.get_file_hash(filepath,filename)
                rom = openvgdb.get_rom_by_hash(hash)
                details["rom_id"] = rom[0]
                details["system_id"] = rom[1]
                #details["name"] = rom[8]
                #details["region"] = rom[13]
                release = openvgdb.get_release_by_rom_id(rom[0])
                details["name"] = release[2]
                details["region"] =  release[4]
                details["front_cover"] = release[7]
                details["back_cover"] = release[8]
                details["description"] = release[11]
                details["developer"] = release[12]
                details["publisher"] = release[13]
                details["genre"] = release[14]
                details["release_date"] = release[15]
                details["gamefaqs"] = release[16]
            json_data = json.dumps(details)
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(get_game_details(), mimetype='text/event-stream')


app.run(threaded=True,host='0.0.0.0', port=8080)

