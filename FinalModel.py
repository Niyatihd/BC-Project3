
import pandas as pd
import numpy as np

import csv
import os



# the data source  will change based on the area selection

df =pd.read_csv(os.path.join("resources","HistoricalData","BayAreaSummary.csv"))
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
Hosuhold_wt = model.coef_[0][1]
Wage_wt = model.coef_[0][2]
Slope = model.intercept_[0]




