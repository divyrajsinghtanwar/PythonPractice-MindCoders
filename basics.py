'''age = 10
per = 10.8
name = "John"
byt= b"Hello"
bt = True 
x=2+1j 
print(age,per,name,byt,bt,x)
print(type(age),type(per),type(name),type(byt),type(bt),type(x))


a = 10
print(a<20 and a>5)
print(a<20 or a>15)
print(not(a<20 and a>5))       


print("") 

m = ["Maruti","BMW"]
n = ["Maruti","BMW"]
o= m
print(m is n)
print(m is o)
print(m is not n)
print(m is not o)

print("")

p = ["Maruti","BMW","Maruti","toyota"]
q="Maruti"
print(q in p)



print("")

j = 17/3

print(j)


j+=2
print(j)

k=10
if(k>5 and k<15):
    print("k is greater than 5 and less than 15")

print(5 & 3)

print(5<<3)
print(5>>3)



x = int(input("Enter a number: "))
print("You entered:", x)
print(type(x))


x = int(input("Enter a height: "))
y = int(input("Enter another width: "))

z = (x**2+y**2)**0.5
print("The value of z is:", z)



print("+------+")
print("|      |")
print("|      |")   
print("|      |")   
print("+------+")   

print("+"+"-"*6+"+")
print(("|"+" "*6+"|\n")*5 ,end="")
print("+"+"-"*6+"+")



x= int(input("Enter a number: "))
y = int(input("Enter another number: "))


if x>y:
    larger_num = x
    smaller_num = y
else:
    larger_num = y
    smaller_num = x

print("")

print("The larger number is:", larger_num)
print("The smaller number is:", smaller_num)


x= int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))

larger_num = x

if y > larger_num:
    larger_num = y
    smaller_num = x
else:
    smaller_num = y

if z > larger_num:
    larger_num = z
    smaller_num = y
    
else:
    smaller_num = x

print("")

print("The larger number is:", larger_num)
print("The smaller number is:", smaller_num)

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))

larger_num = max
(x,y,z)
smaller_num = min(x,y,z)

print("")   
print("The larger number is:", larger_num)
print("The smaller number is:", smaller_num)


largestnum=50

num = int(input("Enter a number (or -1 to stop): "))

while num!=-1:
    if(num>largestnum):
        largestnum = num
    num = int(input("Enter a number (or -1 to stop): "))
print("The largest number is:", largestnum)


a= int(input("Enter a number: "))

count = 1
even = 0
odd = 0
while a>=count and a!=0:
      if count%2==0:
         even += 1
      else:
         odd += 1
      count+=1
print("",odd, "odd",end=" ")   
print("",even,"even",end=" ")

    

for i in range(-12,10,3):
    print(i)
    
pow= 1
for i in range(11):
    pow *= 2
    
    print(pow)
    


for i in range(1,11):
    if(i==2 ):
        break
        print(i)
    print("executed")
    

i = 5
j= not not i
print(j)


#list
y=12
x = [y,12,"Hello",True,1+2j]
print(x)
print(type(x))
x[2] = "World"
print(x)
x[1]=x[4]
print(x)
print(len(x))
del x[3]
print(len(x))
print(x[-1])


x= [1,2,3,4,5]
print(len(x))
del x[-1]
print(len(x))

x[len(x)//2] = int(input("Enter a number: "))
print(x)

list  = [1,2,3,4,5]
print(list)
list.append(6)
print(list)
list.insert(1,12)
print(list)  


lst = [1,2,3,4,5]         //this iterate with the index of the list
for i in range(len(lst)):
    print(lst[i])

for i in lst:         //this iterate with the elements of the list
    print(lst[i-1])


var1 = 11
var2 = 5

var1 ,var2 = var2,var1
print("var1:", var1)
print("var2:", var2)



lst = [1,2,3,4,5]
lst[2],lst[3] = lst[3],lst[2]
print(lst)


lst =[8,10,6,2,4]

swap =True
count = 0
while swap:
    swap = False
    for i in range(len(lst)-1):
        count+=1
        if lst[i]>lst[i+1]:
            swap=True
            lst[i],lst[i+1]=lst[i+1],lst[i]
print(lst)
print(count)

print("")
'''

lst1 = [1]
lst = lst1[:]
lst1[0] = 2
print(lst1)
print(lst)