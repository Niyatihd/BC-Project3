# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:57:22 2018

@author: indra
"""

import pandas as pd
import numpy as np

import numpy as np
import json
import os


# the data source  will change based on the area selection
# If the user does not select an area, 
Area = ""
Year = 2040

if(Area == ""):
    pastTrendFile = "BayAreaSummary.csv"
else:
    pastTrendFile = "CountyLevelSummary.csv"
    

df =pd.read_csv(os.path.join("resources","HistoricalData",pastTrendFile))
df.reset_index(inplace=True, drop=True)
df = df.drop(["Unnamed: 0", "Year"], axis=1)
df_new = df[["Avg.Median Home price","TotalPop","HouseholdPop","EstHouseholds" ,"Net_Migration","Immigration","Interest_Rate"]]
df_new1 = df[["Avg.Median Home price","Domestic_Migration","Employers", "Employees","AvgAnnualPay","New Homes Constructed"]]
Final_df = df[["Avg.Median Home price", "AvgAnnualPay","EstHouseholds", "Employees"]]
Final_df.corr()
X = Final_df[["Employees", "EstHouseholds", "AvgAnnualPay"]]
y = Final_df["Avg.Median Home price"].values.reshape(-1, 1)
#print(X.shape, y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)

# Create the model using LinearRegression

### BEGIN SOLUTION
from sklearn.linear_model import LinearRegression
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

#if the user doesnot select a county, then

if(Area == ""):
    Forecastfile = "BayArea_HH_Jobs_Wage_Forecast.csv"
    ForecastDf = pd.read_csv(os.path.join("resources","BayAreaForecast",Forecastfile))
    ForecastDfSelect = ForecastDf.loc[[ForecastDf['Year'] == Year]]
    MedPrice = ForecastDfSelect["Households"]
else:
    Forecastfile = "County_HH_Jobs_Wage_Forecast.csv" 
    ForecastDf = pd.read_csv(os.path.join("resources","BayAreaForecast",Forecastfile))

print(MedPrice)

# Get the x variables from the forecast Year