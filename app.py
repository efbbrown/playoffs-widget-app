#####################################################
#           Imports                                 #
#####################################################

# Libraries
import sys
import json
import logging
import requests
import requests_toolbelt.adapters.appengine
from flask import Flask, render_template, jsonify, request

# Modules
# from models import db, Project, Session_Info
from config import configure_app
# import functions as funcs

#####################################################
#           Config                                  #
#####################################################

# Initiate the app
app = Flask(__name__)
# Connect the db to the app
# db.init_app(app)
# Set the run_mode of the app - one of "local" or "prod"
if sys.platform == "win32":
    run_mode = "local"
else:
    run_mode = "prod"
# Configure the app
configure_app(app, run_mode)

if run_mode == "prod":
    requests_toolbelt.adapters.appengine.monkeypatch()

#####################################################
#           Views                                   #
#####################################################


@app.route("/")
@app.route("/index/")
def playoffs_widget():
    # r = requests.get("https://data.nba.com/data/v2015/json/mobile_teams/nba/2017/scores/00_playoff_bracket.json")
    # return json.dumps(json.loads(r.text))
    return render_template("index.html")


@app.route("/api/playoff-bracket/")
def api_playoff_bracket():
    logging.info("Getting playoff bracket")
    r = requests.get("https://data.nba.com/data/v2015/json/mobile_teams/nba/2017/scores/00_playoff_bracket.json")
    logging.info("status_code: {0}".format(r.status_code))
    return jsonify(r.json())


@app.route("/api/gamedetail/")
def api_gamedetail():
    gid = request.args.get("gid")
    end_point = "https://data.nba.com/data/v2015/json/mobile_teams/nba/2017/scores/gamedetail/{0}_gamedetail.json".format(gid)
    r = requests.get(end_point)
    return jsonify(r.json())
