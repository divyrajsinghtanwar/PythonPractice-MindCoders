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


def reciprocal(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print("division by zero is not possible")   
        return None
    except Exception as e:
        print("an error has occured :",e)    
        print(e.__str__)
    else:
        print("everything is fine")   
        return n 
    finally:
        print("this will always execute ")

print(reciprocal(2))
print("------------------")
print(reciprocal(0))    
'''

#custom exception
class CustomError(Exception):
    def __init__(self,message):
        self.message = message

def check_positive(n):
    if n<0:
        raise CustomError("the number is negative")
    else:
        print("the number is positive")

check_positive(2)
check_positive(-1)
check_positive(4)
