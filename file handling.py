'''with open("data.txt","r") as file:
    data = file.read()

print(data)


with open("student.txt","w")as file:
    file.write('Rahul Sharma,75,Bhopal\n')
    file.write('harshraj singh tanwer,95,Khandwa\n')
    file.write('abhishek Thhakur,85,Indore\n')

#override the content of the file
with open("student.txt","a")as file:
    file.write("Harshit Buawde,85,Betul\n")

with open("student.txt","r") as f:
    data = f.read()
print(data)    

#for line by line reading for large file    
with open("student.txt","r") as f:
    for line in f:
        name , marks , city = line.strip().split(",")
        print(f"Name: {name}, Marks: {marks}, City: {city}")
        print("-"*30)
        '''

#creating new CSV file
import csv 
records = [
    ['Name','Marks','City','Grade'],
    ['Rahul Sharma',75,'Bhopal','B'],
    ['harshraj singh tanwer',95,'Khandwa','A'],
    ['abhishek Thhakur',85,'Indore','A'],
    ['Harshit Buawde',85,'Betul','A']
]

#writing to CSV file
with open("students.csv","w",newline='') as f:
    csv.writer(f).writerows(records)

#reading CSV file
with open("students.csv","r") as f:
    for row in csv.DictReader(f):
        print(f"Name: {row['Name']},  {row['Marks']} marks, ({row['City']})")    