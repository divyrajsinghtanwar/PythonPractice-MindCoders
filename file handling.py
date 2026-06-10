with open("data.txt","r") as file:
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