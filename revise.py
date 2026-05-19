'''print("Hello, World!\n"*10 , end="finish")


age = int(input("Enter your age: "))

if age >= 40:
    print("You are a senior citizen.")

elif age >=18 and age < 40:
    print("You are an adult.")

elif age>=13 and age <18:
    print("You are a teenager.")

elif age <13 and age >=0:
    print("You are a child.")

else:
    print("Invalid age entered.")
    

st1 = input("Enter a string: ")
M ="Spathiphyllum"

if st1 == M:
    print("Yes - Spathiphyllum is the best plant ever!")

elif st1 == "spathiphyllum":
    print("No -I want a big Spathiphyllum!")

else:
    print("Spathiphyllum! Not "+st1+"!")


st2 = "a"
while st2 < "z":
    print(st2)
    st2=chr(ord(st2)+1)
    
counter = "a"
for i in range(26):
    print(counter)
    counter=chr(ord(counter)+1)        



import time
for i in range(5):
    print(i,"mississippi")
    time.sleep(1)
print("Ready or not, here I come!")    


st3 =(input("Enter a string: "))
st3=st3.upper()

for i in range(len(st3)):
    if st3[i] in "AEIOU":
        continue
    print(st3[i],end="")



lst =[]
nooflements = int(input("Enter the number of elements: "))
for i in range(1,nooflements+1):
    i = int(input("Enter a number: "))
    lst.append(i)
    
print(lst)





lst2 = [10,20,30,40,50]
for i in range(len(lst2)):
    lst2[i] +=  1
print(lst2)    
'''

lst = [10,20,30,40,50,60,70,80,90,100]
sum = 0
for i in range(len(lst)):
    sum += lst[i]
print(sum)