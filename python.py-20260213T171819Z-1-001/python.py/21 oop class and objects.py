######################### OOP
########class and object

class myclass():  #create class
    x=1
print(myclass)

class myclass(): 
    x=1
a=myclass()  #create object
print(a.x)

#__init__() method
class myclass():
    def __init__(self,name,age):
        self.name=name
        self.age=age

mc=myclass("jaga",21)
print(mc.name)
print(mc.age)

#__str__() method
class myclass():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"

mc=myclass("jaga",21)
print(mc)

#create method/function
class myclass():
    def __init__(self,name):
        self.name=name
    def func(self):
        print("name=",self.name)

mc=myclass("jaga")
mc.func()


#modify
class myclass():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("name=",self.name)
        print("age=",self.age)

mc=myclass("jaga",20)
mc.age=21  #modify
mc.func()
"""
#delete
class myclass():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("name=",self.name)
        print("age=",self.age)

mc=myclass("jaga",21)
del mc.age           #delete
mc.func()

del mc               #delete the object
"""
#pass ststement
class myclass():
    pass