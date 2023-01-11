from flask import Flask, request, render_template
import datetime
import configparser
from utils import make_gif
app = Flask(__name__)

config = configparser.ConfigParser()
config.read("config.ini")

@app.route("/", methods=["GET"]) 
def index():
    return render_template("index.html", tab_title=config["server"]["tabtitle"], nav_title=config["server"]["navtitle"], location_subtitle=config["server"]["locationsubtitle"])