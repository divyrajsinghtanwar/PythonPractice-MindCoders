'''
h = int(input("Enter the height of the triangle: "))
for i in range(1,h+1):
    print(" "*(h-i)+"* "*i)

for i in range(51):
    print(i)    
    

for i in range(51):
    print(i,"t")

    

for i in range(51):
    if i ==0:
        continue    
    print(i) 
    if i%2==0:
        print("t") 

for i in range(51):
    if  i%3==0 and i%5==0:
        print("fizzbuzz") 
    elif i%3==0:
        print("fiz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)                   
   



income = float(input("Enter your income: "))
tax = 0.0
if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32
print("The tax is:", tax)


yrs = int(input("Enter the number of years: "))

if yrs % 4==0 and yrs % 100 !=0 or yrs % 400 ==0:
    print(yrs,"is a leap year.")    
else:
    print(yrs,"is not a leap year.")


h = int(input("Enter the height of the triangle: "))
for i in range(1,h+1):
    print(" "*(h-i)+"* "*i)


        
student_record={}
while True:
    name = input("enter name : ")
    if name == "":
        break
    score = int(input(f"enter ${name}'s score:"))

    if score not in range(1,11):
        break   
    if name in student_record:
        student_record[name]+=(score,)
    else:
        student_record[name]=(score,)
    
for name,marks in student_record.items():
    sum = 0
    for m in marks:
        sum += m
    print(name ,"average score is :",sum/len(marks))    

       
student ={}

for i in range(1,6):
    sub = input("enter subject : ")
    student[sub] = int(input(f'enter marks of ${sub} :'))
print(student)    
total=0
failed_subject =[]
for sub ,marks in student.items():
    total +=marks
    if marks<50:
        failed_subject.append(sub)

print("total : ",total)
percentage = (total/500)*100
print("eprcentage :",percentage)

if percentage>=90:
    print("Your grade is : A")
elif percentage >=75:
    print("Your grade is : B")    
elif percentage>=50:
    print("your grade is : c")
else:
    print("you are failed")
    
if len(failed_subject) == 0:
    print("Result : PASS")

else:
    print("Result : FAIL")
    print("Failed subjects :", failed_subject)    
   

Input_String = input("enter string")
dictonary ={}
count =0
lst =[]
for i in range(len(Input_String)):
    if Input_String[i]==" ":
        lst.append(Input_String[count:i])
        count = i+1
        i = count
        continue
print(lst)

for i in range(len(lst)):
    counter =0
    for j in range(len(lst)):
        if lst[i]==lst[j]:
            counter+=1

    if counter >=1:
        dictonary[lst[i]]=(counter,)

print(dictonary)        
'''
