# simple class



class MyClass :
    x= 0
    
call = MyClass()
print(call.x)

# with __init__ method

class Friend :
    def __init__(self, name):
        self.name = name

call1= Friend('Readul Islam')
print(call1.name)

# The __str__() function controls what should be returned when the class object is represented as a string.
class Friends :
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"    

call1= Friends('Readul Islam')
print(call1)

# objects can also contain methods
class Readul:
    def __init__(self, name):
        self.name = name
    def myFun (self):
        print("Hello World ,I am ",self.name)    

getName = Readul('Readul Islam')   
print (getName.myFun())
