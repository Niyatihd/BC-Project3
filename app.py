#################################################
# Import Dependencies
#################################################

import pandas as pd
import numpy as np
import os

import numpy as np
import json
from flask import Flask, render_template, jsonify, request

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

#@app.route("/predictFuture", methods=['GET','POST'])
## the data source  will change based on the area selection
#
#def predictprice():
#    if request.json: ### == 'POST':
#        print("POSTED")
#        #selection = request.json
#        area_selected_json = request.json
#        area_selected = area_selected_json['areaselected']
#        print(area_selected)
#        
#    else:
#        area_selected = ""
#        
#    returnval = {"name":area_selected}
#    
#    return jsonify(returnval)


@app.route("/predictFuture", methods=['GET','POST'])
# the data source  will change based on the area selection
def predictprice():
    if request.json: ### == 'POST':
        print("POSTED")
        #selection = request.json
        area_selected_json = request.json
        area_selected = area_selected_json['areaselected']
        print(area_selected)
        
        if area_selected == "" or area_selected == "Bayarea":
            pastTrendFile = "BayAreaSummary.csv"

            df =pd.read_csv(os.path.join("resources","HistoricalData",pastTrendFile))
            df.reset_index(inplace=True, drop=True)
            df = df.drop(["Unnamed: 0", "Year"], axis=1)
            Final_df = df[["Avg.Median Home price", "AvgAnnualPay","EstHouseholds", "Employees"]]
    
            #The predictor variables/features are "Employees", "EstHouseholds", "AvgAnnualPay" and dependent variable is Avg Median Home Price
            X = Final_df[["Employees", "EstHouseholds", "AvgAnnualPay"]]
            y = Final_df["Avg.Median Home price"].values.reshape(-1, 1)
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)
            
            # Create the model using LinearRegression  
            model = LinearRegression()
        
            # Fit the model to the training data and calculate the scores for the training and testing data
            model.fit(X_train, y_train)

            Employees_wt= model.coef_[0][0]
            Household_wt = model.coef_[0][1]
            Wage_wt = model.coef_[0][2]
            y_intercept = model.intercept_[0]

            #return result     
            result = {"employees_wt":Employees_wt, "household_wt":Household_wt, "wage_wt":Wage_wt, "y-intercept":y_intercept}  
            print(result)
        
        # If the user does not select an area,     
        else:
            pastTrendFile = "CountyLevelSummary.csv"
            df =pd.read_csv(os.path.join("resources","HistoricalData",pastTrendFile))
            df.reset_index(inplace=True, drop=True)
            df = df.drop(["Unnamed: 0", "Year"], axis=1)
            
            variables_df = df[["Avg.Median Home price", "AvgAnnualPay","EstHouseholds", "Employees"]]
            Final_df = variables_df.loc[df["County"] == area_selected]
    
            #The predictor variables/features are "Employees", "EstHouseholds", "AvgAnnualPay" and dependent variable is Avg Median Home Price
            X = Final_df[["Employees", "EstHouseholds", "AvgAnnualPay"]]
            y = Final_df["Avg.Median Home price"].values.reshape(-1, 1)
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=31)
            
            # Create the model using LinearRegression  
            model = LinearRegression()
        
            # Fit the model to the training data and calculate the scores for the training and testing data
            model.fit(X_train, y_train)
            training_score = model.score(X_train, y_train)
            testing_score = model.score(X_test, y_test)
            #print(f"Training Score: {training_score}")
            #print(f"Testing Score: {testing_score}")
            
            Employees_wt= model.coef_[0][0]
            Household_wt = model.coef_[0][1]
            Wage_wt = model.coef_[0][2]
            y_intercept = model.intercept_[0]
            
            result = {"employees_wt":Employees_wt, "household_wt":Household_wt, "wage_wt":Wage_wt, "y-intercept":y_intercept}
            print(result)

            
    return jsonify(result)
        

if __name__ == "__main__":
    app.run(debug=True)