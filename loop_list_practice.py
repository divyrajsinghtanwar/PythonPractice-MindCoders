'''
#list 

#1
hat_lst=[1,2,3,4,5]
print(len(hat_lst))

#2
del hat_lst[-1]
print(hat_lst)

#3
mdl= len(hat_lst)//2
intbyuser = int(input("Enter number:"))
hat_lst.insert(mdl,intbyuser)
print(hat_lst)


#beatles list

#1
beatles = []

#2
beatles.append("John lennon")
beatles.append("paul Mc Cartney")
beatles.append("George Harrision")
print(beatles)
print("")

#3
for i in range(2):
    band = input("Enter Band:")
    beatles.append(band)
print(beatles)
print(" ")
#4
del beatles[-2:]
print(beatles)
print(" ")

#5
beatles.insert(0,"Ringo Starr")
print(beatles)


#practice loop
loop_pract = []
for i in range(1,51):
    if  i%3==0 and i%5==0:
        loop_pract.append("fizzbuzz") 
    elif i%3==0:
        loop_pract.append("fiz")
    elif i%5==0:
        loop_pract.append("buzz")
    else:
        loop_pract.append(i) 

print(loop_pract)             



#count number of digit in string

#1
string ="MindCoders Password2 is: 1234"
digit = ['0','1','2','3','4','5','6','7','8','9']
count = 0
for i in range(len(string)):
    if string[i] in digit:
        count += 1
print("total number of Digits : ",count)

#2
inp_string ="U r a a n S 0 f t s k i l l 1 s 1234"
count1 = 0
for i in range(len(inp_string)):
    if inp_string[i] in digit:
        count1+=1
print("total number of digits : " ,count1)

#3
count2 = 0
inp_match = ['S','s']
for i in range(len(inp_string)):
    if inp_string[i] in inp_match:
        count2 += 1
print(count2)        



#advance loop practice
inp_string2 ="UraanSoftskills"
unique = 0
repeated =0
for i in range(len(inp_string2)):
    count3=0
    for j in range(len(inp_string2)):
            if inp_string2[i]==inp_string2[j]:
                count3+=1

    if count3==1:
          unique+=1

    else:
          repeated+=1
print("unique : ",unique)
print("repeated : ",repeated)


#vowel eater 
# strforv = input("enter string : ").upper()
# vowel = ['A','E','I','O','U']
# without_vowel =""
# for i in range(len(strforv)):
#     for j in range(len(vowel)):
#         if strforv[i] ==vowel[j] :
#             del strforv[i]
#             continue
#         else:
#             print(strforv)

#basic loop question
#1
for i in range(1,11):
   print(i)

#2
for i in range(11):
   if i%2==0:
      print(i)   

sum =0
for i in range(16):
    sum+=i
print("sum of all number is : ",sum)   


table_num=15
for j in range(11):
    print("15 * ",j," is : ",15*j)

lstofnum = [1,2,4,6,88,125]
for i in lstofnum:
    print(i)

number =str(129475)
count = 0
for i in range(len(number)):
    count+=1
print(count)    

palstr = "madam"
count =0
for i in range(len(palstr)): # mene 2 loop laga diye the
    if(palstr[i] ==palstr[-(i+1)]):
        count+=1
if count ==len(palstr):
    print("string is palendrom:",palstr) 
else:
    print("string is not palendrom")           

# usertoreverse = input("enter string : ")
# for i in range(len(usertoreverse)):
#     usertoreverse[i],usertoreverse[-i]=usertoreverse[-i],usertoreverse[i]
# print(usertoreverse)    


armsno=input("enter armstrong number : ")
sum =0
for i in range(len(armsno)):
    digit =int(armsno[i])
    cube = digit**3
    sum +=cube
if sum == int(armsno):
    print(armsno,":is armstrong number")
else:
    print(armsno,":is not armstrong number")        '''
