#################################################
# Import Dependencies
#################################################

import pandas as pd
import numpy as np
import os

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

@app.route("/predictFuture", methods=['GET','POST'])
# the data source  will change based on the area selection

def predictprice():
    if request.json: ### == 'POST':
        print("POSTED")
        #selection = request.json
        area_selected_json = request.json
        area_selected = area_selected_json['areaselected']
        print(area_selected)
        
    else:
        area_selected = ""
        
    returnval = {"name":area_selected}
    
    return jsonify(returnval)



if __name__ == "__main__":
    app.run(debug=True)