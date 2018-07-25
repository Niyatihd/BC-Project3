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
        
        if area_selected == "Bay Area" or area_selected == "":
            pastTrendFile = "BayAreaSummary.csv"

            df =pd.read_csv(os.path.join("resources","HistoricalData",pastTrendFile))
            #            df =pd.read_csv(os.path.join("resources","HistoricalData",pastTrendFile))

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
            result = {"employees_wt":Employees_wt, "household_wt":Household_wt, "wage_wt":Wage_wt, "y_intercept":y_intercept}  
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
            
        # get the jobs, HH and wages forecast for 2020, 2025, 2030, 2035 and 2040 and claulate median HH price and Qualifying income
        ForecastDf = pd.read_csv(os.path.join("resources","BayAreaForecast","County_HH_Jobs_Wage_Forecast_Updated.csv"))
        #Assuming the Interest rates hold steady into the future.
        interestRate = 4.46
                
        ForecastDF = pd.read_csv(os.path.join("resources","BayAreaForecast","County_HH_Jobs_Wage_Forecast_Updated.csv"))
        #ForecastDF = CountyLevelDF.drop(["Unnamed: 0"], axis=1)
        ForecastDF = ForecastDF[["Year","County","AvgAnnualPay","Jobs","Households"]]
        ForecastDF = ForecastDF.loc[ForecastDF["County"] == area_selected]
        ForecastDF = ForecastDF.loc[ForecastDF["Year"] >2015]
        ForecastDF ["Avg.Median Home price"] = y_intercept + (ForecastDF["AvgAnnualPay"]*Wage_wt) + (ForecastDF["Jobs"]*Employees_wt) +(ForecastDF["Households"]*Household_wt)
        
        
        ForecastDF["MedLoanAmt"] = ForecastDF["Avg.Median Home price"] - ForecastDF["Avg.Median Home price"]*0.2
        ForecastDF["MthlyMortPay"] =  np.round((np.pmt(interestRate/1200,360,ForecastDF["MedLoanAmt"]))*(-1))
        ForecastDF["MthlyTax"]  =  np.round(ForecastDF["Avg.Median Home price"]*0.01)/12
        ForecastDF["MthlyIns"]  =np.round(ForecastDF["Avg.Median Home price"] * 0.0038)/12
        ForecastDF["MthlyHousingCost"] = ForecastDF["MthlyMortPay"] +ForecastDF["MthlyTax"] +ForecastDF["MthlyIns"] 
        ForecastDF["MthlyMinIncome"]=  np.round(ForecastDF["MthlyHousingCost"]/0.3)
        ForecastDF["Qualifying Income"] = ForecastDF["MthlyMinIncome"]*12
        ForecastDF = ForecastDF[["Year","Avg.Median Home price","Qualifying Income","AvgAnnualPay"]]
        ForecastDF
        
        ForecastDF.set_index('Year',inplace=True)
        ForecastDFTransposed = ForecastDF.transpose()
        ForecastDFTransposed = ForecastDFTransposed.round()
        return jsonify(ForecastDFTransposed.to_html())    
    #result = {"employees_wt":Employees_wt, "household_wt":Household_wt, "wage_wt":Wage_wt, "y_intercept":y_intercept}
            #print(result)

            
   # return jsonify(result)

@app.route("/plotlyData")
# the data source  will change based on the area selection
def getYearlyData():
    data_df = pd.read_json("static/resources/HH_Jobs_Income_MedHHPrice_PctChange_91_16.json")
    data_df.Year = data_df.Year.astype(float)
    counties = ['Bay Area', 'Solano', 'Sonoma', 'Santa Clara', 'San Mateo',
                'San Francisco', 'Napa', 'Marin', 'Contra Costa', 'Alameda']
    final_dict = {}
    for county in counties:
        temp_dict = {}
    #     print(county)
        current_df = data_df.loc[data_df["County"] == county]
        year_list = current_df['Year'].tolist()       
        house_list = current_df['Households'].tolist() 
        income_list = current_df['Income'].tolist() 
        jobs_list = current_df['Jobs'].tolist()
        homeprice_list = current_df['Median Home Price'].tolist()
        temp_dict["year"] = year_list
        temp_dict["household"] = house_list
        temp_dict["income"] = income_list
        temp_dict["jobs"] = jobs_list
        temp_dict["medianHomePrice"] = homeprice_list
        final_dict[county] = temp_dict
        print(temp_dict)
    # final_dict    
            
    print(final_dict)
            
#    final_plotly_list.append(parent_dict)
#    print(final_plotly_list)
    return jsonify(final_dict)


@app.route("/plot2Data")
# the data source  will change based on the area selection
def getYearlyDataPlot2():
    data_df1 = pd.read_csv("resources/BayAreaForecast/MinimumQualifyingIncomePastANDFuture_5YrIntervals.csv")
    data_df1.Year = data_df1.Year.astype(float)
    data_df1["Avg.Median Home price"] = data_df1["Avg.Median Home price"].astype(float)
    data_df1["QualifyingIncome"] = data_df1["QualifyingIncome"].astype(float)
    data_df1["AvgAnnualIncome"] = data_df1["AvgAnnualIncome"].astype(float)
    counties1 = ['Bay Area', 'Solano', 'Sonoma', 'Santa Clara', 'San Mateo',
                'San Francisco', 'Napa', 'Marin', 'Contra Costa', 'Alameda']
    final_dict1 = {}
    for county in counties1:
        temp_dict1 = {}
    #     print(county)
        current_df1 = data_df1.loc[data_df1["County"] == county]
        year_list1 = current_df1['Year'].tolist()       
        avg_income_list1 = current_df1['AvgAnnualIncome'].tolist() 
        qualifying_income_list1 = current_df1['QualifyingIncome'].tolist() 
        homeprice_list1 = current_df1['Avg.Median Home price'].tolist()
        temp_dict1["year"] = year_list1
        temp_dict1["avgAnnualIncome"] = avg_income_list1
        temp_dict1["qualifyingIncome"] = qualifying_income_list1
        temp_dict1["medianHomePrice"] = homeprice_list1
        final_dict1[county] = temp_dict1
        print(temp_dict1)
    # final_dict   
            
    print(final_dict1)
            
#    final_plotly_list.append(parent_dict)
#    print(final_plotly_list)
    return jsonify(final_dict1)
        

if __name__ == "__main__":
    app.run(debug=True)