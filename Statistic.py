import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
'''
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
'''
#correlation

np.random.seed(42)
study = np.random.uniform(2,10,60)
marks = study*8+np.random.normal(0,10,60)
marks = np.clip(marks,30,100)
absent = 10 - study +np.random.normal(0,1,60)

df = pd.DataFrame({'Study_Hours':study,'Marks':marks,'Absences':absent})

corr_matrix = df.corr()
print(corr_matrix.round(3))

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix,annot = True,cmap='coolwarm',vmin=-1,vmax=1,fmt='.2f')
plt.title('correlation matrix');plt.show()

r,p_value = stats.pearson(study,marks)
print(f'study-marks correlation : r ={r:.3f},p={p_value:.4f}')
print('Interpretation:','strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'Weak')
 