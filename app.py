#################################################
# Import Dependencies
#################################################
import datetime as dt
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,inspect, func

import numpy as np
import json
from flask import Flask, render_template, jsonify, request

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def index():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)