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
## If the user does not select an area, 
#    pastTrendFile = "BayAreaSummary.csv"
#    #else:
#    #pastTrendFile = "CountyLevelSummary.csv"
#    # Area = "UserArea"
#    #Year = "UserYear"
#    
#    df =pd.read_csv(os.path.join("resources","HistoricalData",pastTrendFile))
#    df.reset_index(inplace=True, drop=True)
#    df = df.drop(["Unnamed: 0", "Year"], axis=1)
##    df_new = df[["Avg.Median Home price","TotalPop","HouseholdPop","EstHouseholds" ,"Net_Migration","Immigration","Interest_Rate"]]
##    df_new1 = df[["Avg.Median Home price","Domestic_Migration","Employers", "Employees","AvgAnnualPay","New Homes Constructed"]]
#    Final_df = df[["Avg.Median Home price", "AvgAnnualPay","EstHouseholds", "Employees"]]
#    Final_df.corr()
#    X = Final_df[["Employees", "EstHouseholds", "AvgAnnualPay"]]
#    y = Final_df["Avg.Median Home price"].values.reshape(-1, 1)
#    #print(X.shape, y.shape)
#    
#    from sklearn.model_selection import train_test_split
#    
#    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)
#    
#    # Create the model using LinearRegression
#    
#    ### BEGIN SOLUTION
#    from sklearn.linear_model import LinearRegression
#    model = LinearRegression()
#    
#    
#    # Fit the model to the training data and calculate the scores for the training and testing data
#    
#    
#    model.fit(X_train, y_train)
#    training_score = model.score(X_train, y_train)
#    testing_score = model.score(X_test, y_test)
#    
#    #print(f"Training Score: {training_score}")
#    #print(f"Testing Score: {testing_score}")
#    
#    Employees_wt= model.coef_[0][0]
#    Household_wt = model.coef_[0][1]
#    Wage_wt = model.coef_[0][2]
#    
#    # if the user doesnot select a county, then
#    #Forecastfile = "BayArea_HH_Jobs_Wage_Forecast"
#    #Forecastfile = "County_HH_Jobs_Wage_Forecast"    
#    
#    #ForecastDf = pd.read_csv(os.path.join("resources","BayAreaForecast",ForecastFile))
#    
#    # Get the x variables from the forecast Year
#    result = {"employees_wt":Employees_wt, "household_wt":Household_wt, "wage_wt":Wage_wt}
#    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)