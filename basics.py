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

#swapping
var1 = 11
var2 = 5
var1 ,var2 = var2,var1
print("var1:", var1)
print("var2:", var2)

lst = [1,2,3,4,5]
lst[2],lst[3] = lst[3],lst[2]
print(lst)



#Bubble sort
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

#slice  
lst1 = [1]
lst = lst1[:] #start:end
lst1[0] = 2
print(lst1)
print(lst)

lst2 = [1,2,3,4,5]
print(lst2[1:4])
print(lst2[:3])
print(lst2[3:])
print(lst2[-5:-1])

del lst2[1:4]
print(lst2)

print(5 in lst2)
print(6 in lst2)
print(5 not in lst2)
print(6 not in lst2)


#list comprehenshion
row =[]
for i in range(8): 
   row.append("white pawn")

print(row)


row= ["white pawn" for i in range(8)]
square =[x**2 for x in range(8)]


#2-D array
board = []
for i in range(8):
    row = ["EMPtY" for i in range(8)]
    board.append(row)

for index in board:
    print(index)    

print("-----------------------------")


board[0][0]="B Rooks"
board[0][7]="B Rooks"
board[7][0]="W rooks"
board[7][7]="W rooks"

board[0][1]="B knight"
board[0][6]="B knight"
board[7][1]="W knight"
board[7][6]="W knight"

board[0][2]="B Bishop"
board[0][5]="B Bishop"
board[7][2]="W Bishop"
board[7][5]="W Bishop"

board[0][3]="B king"
board[0][4]="B Queen"
board[7][3]="W King"
board[7][4]="W Queen"

board[1] =["B Pawn" for i in range(8)]
board[6] =["W Pawn" for i in range(8)]


print(board)

#list list comprension
temp = [[ 0.0 for i in range(24)]for d in range(31)]
temp1 = 30
temp2 = 32
count = 0

for day in temp:
    if count ==0:
        day[11]=temp1
        count=1
    else:
        day[11] = temp2
        count = 0 

for element in temp:
    print(element)           
    
total = 0.0
for day in temp:
    total+=day[11]
average = total/31        
print("avg temp temp at noon:",average)

highest=-100
for day in temp:
    for temp in day:
        if highest<temp:
            highest=temp

print(highest)            

hot_doys = 0
for day in temp:

#list list list comprehension
room =[[[False for r in range(20)] for f in  range(15)] for t in range(3)]
print(room)

room[1][9][13] = True
room[1][9][1] = True

vacant_rooms = 0
for room_number in range(20):
    if not room[1][9][room_number]:
        vacant_rooms += 1
print("Number of vacant rooms:", vacant_rooms)


#function

#function declaration
def message():
    print("enter value:")
    temp = int(input())
    return temp

#function invokation
a=message()    

    
b = message()

print("a:",a)
print("b:",b)


def message1():
    print("Enter a value:")
print("we start here. ")
#message1=1
print(message1)#give memory address  
message1()
print("we end here . ")  

 
 #argument - parametrized function 
def hello(n):#parameter
  print("hello",n)

name = input("enter name:")
hello(name) #argument-carries value

def message(what ,number):
  print("enter",what ,"number",number)

message("telephone",11)
message(11,"teephone")
message("price",5) 
message("number","number") 

def introduction(first_name,last_name):
  print("hello ,my name is ",first_name,last_name)

introduction("luke","skywalker")
introduction("jesse","quick")  

#keyword argument passing
introduction(first_name="james",last_name="bond")
introduction(last_name="skywalker",first_name="luke")
#introduction("divy",first_name="tanwer")
introduction("divy",last_name="tanwer")


def intro(a="james bond",b="bond"):
  print("My name is ",b+".",a+".")

intro() #use default value

def add_number(a,b=2,c):#syntax error
  print(a+b+c)
add_number(a=1,c=3)  


def happ_new_year(wishes = True):
  print("three...")
  print("two")
  print("one")
  if not wishes:
    return
  print("happ new year")

happ_new_year(False)  


#passing list as argument
def lst_sum(lst):
    s=0

    for elem in lst:
        s+=elem

    return s
print(lst_sum([5,4,3]))    

def strange_list_fun(n):
    strange_list=[]

    for i in range(0,n):
        strange_list.insert(0,i+1)
        strange_list.append(i+1)

    return strange_list
print(strange_list_fun(5))

def is_int(data):
    if type(data)==int:
       return True
    elif type(data)==float:
       return False
    
print(is_int(5))
print(is_int(5.0))
print(is_int("str"))    //None


#scope
def scope_test():
    x =12   #onlyu accessible inside loop(locally)
    print("do i know variable",varsc)

varsc = 1    #accessible gobally even inside function
scope_test()
#print(x)    #variable not defined
print(varsc)

def mul(x):
    var = 7 
    return x*var
var =3
print(mul(7))


#making variable globally- it extend accessiblity/scope
def my_function():
    global varg
    varg=2
    print("do i know variable",varg)
varg=1
my_function()
print(varg)    #2

def my_function(n):
    print("i got:",n)
    n+=1
    print("I have:",n)
var = 1
my_function(var)
print(var)    

def my_function(my_lst1):
    print("print #1:",my_lst1)
    print("print #2:",my_lst2)
    my_lst1=[0,1]
    print("print #3:",my_lst1)
    print("print #4:",my_lst2)

my_lst2=[2,3]
my_function(my_lst2)
print("print #5:",my_lst2)  
print(" ")  

def my_function(my_lst_1):
    print("print #1:",my_lst_1)
    print("print #2:",my_lst_2)
    del my_lst_1[0]  #pay attention 
    print("print #3:",my_lst_1)
    print("print #4:",my_lst_2)

#Recursion
my_lst_2=[2,3]
my_function(my_lst_2)
print("print #5:",my_lst_2)    


def rec_fun(n):    
    print(n)

 
    if(n==0):
        return 
    else:
        print("going in rec:",n)
        rec_fun(n-1)
        print("out of rec :",n)
    
rec_fun(5)
'''
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
    
    