import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    'Marks' : np.random.randint(40,100,100),
    'Study_Hours' : np.random.uniform(2,10,100),
    'City' : np.random.choice(['Bhopal','Indore','Jabalpur'],100),
    'gender' : np.random.choice(['male','Female'],100)
})
'''
plt.figure(figsize=(10,4))
sns.histplot(df['Marks'],bins =20,kde=True,color='steelblue')
plt.title('Distribution of student marks')
plt.show()

#box plot 
sns.boxplot(data=df,x ='City',y = 'Marks',palette='Set2')
plt.title('Marks Distribution by city')
plt.show()
'''
#correlation heatmap 
plt.figure(figsize=(5,4))
sns.heatmap(df[['Marks','Study_Hours']].corr(),annot = True,cmap='coolwarm',vmin = -1,vmax=1)
plt.title('Correlation Matrix')
plt.show()

#pair plot
sns.pairplot(df[['Marks','Study_Hours']],diag_kind='kde')
plt.show()