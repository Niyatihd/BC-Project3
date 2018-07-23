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

@app.route("/plotlyData")
# the data source  will change based on the area selection
def getYearlyData():
    data_df = pd.read_json("static/resources/County_HH_Jobs_Income_MedHHPrice_PctChange_91_16.json")
    data_df.Year = data_df.Year.astype(float)
    count = 0
    child_dict = {}
    parent_dict = {}
#    final_plotly_list = []
    
    current_county = data_df.County[count]
    child_dict["year"] = [data_df.Year[count]]
    child_dict["Households"] = [round(data_df.Households[count],2)]
    child_dict["Income"] = [round(data_df.Income[count],2)]
    child_dict["Jobs"] = [round(data_df.Jobs[count],2)]
    child_dict["Median Home Price"] = [round(data_df["Median Home Price"][count],2)]
    
    for x in range(len(data_df.County)):
        
    
    #     print(data.County[x])
        if data_df.County[x] == current_county:
    #         county_list.append(data.County[x])
            child_dict["year"].append(data_df.Year[x])
            child_dict["Households"].append(round(data_df.Households[x],2))
            child_dict["Income"].append(round(data_df.Income[x],2))
            child_dict["Jobs"].append(round(data_df.Jobs[x],2))
            child_dict["Median Home Price"].append(round(data_df["Median Home Price"][x],2))
            
        else:
            parent_dict[data_df.County[x]] = child_dict
            count += 1    
            
    print(parent_dict)
            
#    final_plotly_list.append(parent_dict)
#    print(final_plotly_list)
    return jsonify(parent_dict)
        

if __name__ == "__main__":
    app.run(debug=True)