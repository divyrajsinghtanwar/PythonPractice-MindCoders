'''class ExampleOfExceptionClass:
    def __init__(self,val = 1):
        self.__first = val
        if val%2!=0:
            self.a = 1
        else:
            self.b = 1    

example_obj = ExampleOfExceptionClass(6)

try:
    print("a=",ExampleOfExceptionClass.a)
except AttributeError:
    try:
        print("b=",ExampleOfExceptionClass.b)
    except AttributeError:
        print("the error has occured ! silently passing it")    
#hasattr
class ExampleOfExceptionClass:
    def __init__(self,val = 1):
        self.__first = val
        if val%2!=0:
            self.a = 1
        else:
            self.b = 1    

example_obj = ExampleOfExceptionClass(6)
hasattr(myobj,'ExampleOfExceptionClass')
if hasattr(example_obj,'a'):
    print("a = ",example_obj.a)

if hasattr(example_obj,'b'):
    print("b = ",example_obj.b)    

class ExampleOfExceptionClass:
    a =1
    def __init__(self,val = 1):
        #self.__first = val
        if val%2!=0:
            self.a = 1
        else:
            self.b = 1    

example_obj = ExampleOfExceptionClass(1)

if hasattr(example_obj,'a'):
    print("a = ",example_obj.a)

if hasattr(example_obj,'b'):
    print("b = ",example_obj.b)  
'''
#name mangling - to access hidden propert
class Classy:
    def visible(self):
        print("this is a visible method")
    def __hidden(self):
        print("this is a hidden method")

obj = Classy()
print(type(obj))
print(type(obj).__name__)
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()       
