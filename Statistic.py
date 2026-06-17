import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#central tendency 
mean = np.mean(salaries) #Average
median = np.median(salaries)  #middle value when sorted
mode = stats.mode(salaries,keepdims=True).mode[0] #Most frequent

print(f'mean :Rs.{mean:.1f}k')
print(f'Median : Rs.{median}k')
print(f'Mode : Rs.{mode}k')


#spread  - how varied is the data?
std = np.std(salaries)  #standard deviation
var = np.var(salaries)  #variance
rng = max(salaries)-min(salaries)  #25th percentile
q1 = np.percentile(salaries,25)
q3 = np.percentile(salaries,75)
iqr = q3 - q1
print(f'std deviation : {std :.2f}k')
print(f'IQR: {iqr}k (Q1 = {q1},Q3 ={q3})')


#Outlier detection using IQR (Interquartile range = q3-q1)
lower = q1 - (1.5*iqr)
upper = q3 + (1.5*iqr)
outliers = [x for x in salaries if x<lower or x>upper]
print(f'Outlier :{outliers}')
print(" ")
print("lower :",lower)
print('upperr :',upper)