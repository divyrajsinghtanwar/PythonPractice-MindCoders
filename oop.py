'''class MyFirstClass:
    name ="Divy"
    age =20

    def getName(self):
        print(self.name)

firstobj = MyFirstClass()
print(firstobj)

firstobj.getName()
print(firstobj.name)


class student:
    def __init__(self,name,age,gender,gradeh):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade
 
    def printdata(self):  
        print(divyraj.name)
        print(divyraj.age)
        print("gender",divyraj.gender)
        print("grade",divyraj.grade)    

divyraj = student("divy ",20,"male","4 th year")
print(divyraj)
divyraj.printdata()

# divyraj.name = "Divyraj singh tanwar"
# divyraj.age = 20
# divyraj.gender = "male"
# divyraj.grade = "Btech final year"

# print(divyraj.name)
# print(divyraj.age)
# print(divyraj.gender)
# print(divyraj.grade)


class ExampleClass :
    def __init__(self,val = 1):
        self.first = val

    def set_second(self,var):
        self.second=var1    

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
       

class Classy:
    varia = 2
    def method(self,par):  #alway give self as parameter otherwise it give error
        print("method ",par) 

    method(2,1)           

obj = Classy()
obj.method(1) 



class Classy1:
    varia = 2
    def method(self):
        print(self.varia, self.var)
obj = Classy1()
obj.var = 3
obj.method()     


class Star:
    def __init__(self,name,galaxy):
        self.name  = name
        self.galaxy = galaxy

    def  __str__(self):
        return self.name + 'in' + self.galaxy    

sun  = Star("Sun","milky man")        
print(sun)




#Inheritance
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class  TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
    for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
        print(issubclass(cls1,cls2),end  = "\t")

    print()    


class Super:
    supVar =1
    
class sub(Super):
    subVar = 2

obj = sub()
print(obj.subVar)
print(obj.supVar)

#constructor chaining

class Super:
    def __init__(self):
        self.superVar = 11

class sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12
obj = sub()
print(obj.subVar)
print(obj.superVar)


#multilevel inheritance
class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102

class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2(self):
        return 202

class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__() 
        self.var_3 = 301
    def fun_3(self):
        return 302

obj = Level3()
print(obj.variable_1,obj.var_1,obj.fun_1())        
print(obj.variable_2,obj.var_2,obj.fun_2())
print(obj.variable_3,obj.var_3,obj.fun_3())

#class variable
class ExampleClass:
    counter = 0
    def __init__(self,val = 1):
        self.__first = val
        if val%2!=0:
            self.a = 1
        else:
            self.b = 1    
        ExampleClass.counter +=1


example_obj = ExampleClass(6)
#print(example_obj.a)
print(example_obj.b)


example_obj1 = ExampleClass()
example_obj2 = ExampleClass(2)
example_obj3 = ExampleClass(4)

print(example_obj1.__dict__,example_obj1.counter)
print(example_obj2.__dict__,example_obj2.counter)
print(example_obj3.__dict__,example_obj3.counter)
'''

#private class
class python:
    population=1
    def __init__(self):
        self.lenght_ft = 3
        self.__venomous = False    #accesing private class

myobj = python()
print("myobj.population :",myobj.population)
print("myobj.lenght_ft : ",myobj.lenght_ft) 
#print("myobj.__venoums:",myobj.__venomous)
#print("myobj.venoums:",myobj.venomous)       

#but in python we can access private class by writing obj._Class_Name__Private_class
print("myobj.__venoums:",myobj._python__venomous)


#isinstance method
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
My_tracked_vehicle =TrackedVehicle()

for obj in [my_vehicle,my_land_vehicle,My_tracked_vehicle]:
    for cls in [Vehicle,LandVehicle,TrackedVehicle]:
        print(isinstance(obj,cls),end = "\t")
    print()

#is operator
class SampleClass:
    def __init__(self,val):
        self.val = val            
obj_1 = SampleClass(0)
obj_2 = SampleClass(2)
obj_3 = obj_1
obj_3.val +=1

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_3 is obj_1)
print(obj_1.val,obj_2.val,obj_3.val)

string_1 = "marry is "
string_2 = "marry is lamb"
string_1+="lamb"

print(string_1 == string_2,string_1 is string_2)