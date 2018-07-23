# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:43:46 2018

@author: indra
"""

import pandas as pd
import numpy as np

# Change MedianHomePrice as  needed.
medianHomePrice = 1610000

# Assuming 20% down paymnet - Does not change
downpayment = 20

loanAmount = medianHomePrice - ((medianHomePrice*downpayment)/100)

# Assuming that today's 30 year fixed interest rates into future - Does not change
interest = 4.93

monthlyMortgagePayment = np.round((np.pmt(interest/1200,360,loanAmount))*(-1))

#Assuming 1% property taxes
propertyTaxes  = np.round(medianHomePrice*0.01)/12

#Assuming 0.38 percent insurance payment
insurancePayment = np.round(medianHomePrice * 0.0038)/12

totalMonthyHousingCost = monthlyMortgagePayment +propertyTaxes+insurancePayment

#minimum monthly salary you need to afford to own a home at the meadian price level
minimumMonthlyIncome = np.round(totalMonthyHousingCost/0.3)

#minimum annual salary you need to afford to own a home at the meadian price level
minimumAnnualIncome = minimumMonthlyIncome*12


print((monthlyMortgagePayment/0.3) *12)