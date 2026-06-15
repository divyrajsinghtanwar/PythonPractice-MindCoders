import pandas as pd

data = {
    'Name': ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age' : [22 , 21 , 23 ,20,24],
    'Marks' : [85,92,78,88,73],
    'City' : ['Bhopal','Indore','Bhopal','Jabalpur','Indore'], 
}

df = pd .DataFrame(data)
'''
print(df)
print("-"*20)

#explore the data
print(df.shape)
print("")

print(df.head(3))
print(" ")

print(df.dtypes)
print("-"*20)

print(df.describe())
'''

#select columns 
print("df['Name']:\n",df['Name'])
print("-"*20)
print(df[['Name','Marks']]) #multiple column
print("-"*20)

#Filter rows
print(df[df['Marks']>=85])
print("-"*20)
print(df[df['City'] =='Bhopal'])
print("-"*20)
print(df[(df['Marks']>=80) &(df['City']=='Indore')])
print("-"*20)

def get_grade(x):
    if x<=90:
        return 'A'
    elif x>=75:
        return 'B'
    else:
        return 'C'
    
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print("-"*20)
print(df)    
print("-"*20)

#GroupBy - like excel pivot
city_avg  = df.groupby('City')['Marks'].mean()
print(city_avg)

#Read real csv file
df2 = pd.read_csv('students.csv')

df2['Name']=df2['Name'].str.strip()
df2['Marks'] = df2['Marks'].str.replace('#','')
df2['City'] = df2['City'].str.strip()



df2.to_csv('clean_output.csv',index=False)  #save 