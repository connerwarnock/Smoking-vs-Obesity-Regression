# Author: Conner Warnock
# Quick program charting smoking vs obesity rates by country, with a linear regression. Couldn't find any graphs
# on the subject on Google after a conversation with a friend, and decided to do a quick look at it myself!
# Date: Oct 12, 2020

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

ob_data = pd.read_csv("WHO_obesityByCountry_2016.csv")
ob_data = ob_data.drop(columns=['Male','Female'])
ob_data = ob_data.rename(columns={"Unnamed: 0": "Entity"})
ob_data = ob_data.rename(columns={"Both.sexes": "ObesityRate"})
#print(ob_data.info())
#print(ob_data.head())

sm_data = pd.read_csv("prevalence-of-tobacco-use-sdgs.csv")
#print(sm_data.info())
sm_data = sm_data[sm_data.Year == 2016]
sm_data = sm_data.rename(columns={"3.a.1 - Age-standardized prevalence of current tobacco use among persons aged 15 years and older, by sex (%) - SH_PRV_SMOK - Both sexes": "SmokingRate"})
#print(sm_data.head())

comb_data = pd.DataFrame()
comb_data = pd.merge(ob_data, sm_data, how ='inner', on ='Entity')
print(comb_data.info())

x = comb_data.SmokingRate
y = comb_data.ObesityRate
plt.scatter(x,y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
predict_y = intercept + slope * x
print(r_value**2)
plt.plot(x,p(x),"r--")
plt.show()
