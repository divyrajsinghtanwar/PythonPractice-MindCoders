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


        '''
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

            