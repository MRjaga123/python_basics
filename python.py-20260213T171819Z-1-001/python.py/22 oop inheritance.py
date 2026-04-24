#OOP
#inheritance

#create parent class
class parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print("name=",self.name)
        print("age=",self.age)

p=parent("jaga",21)
p.print()

#create parent and child class
class parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print("name=",self.name)
        print("age=",self.age)
class child(parent):
    pass

c=child("zoro",3)
c.print()

#__init__()
class parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
class child(parent):
    def __init__(self, name, age):
        parent.__init__(self,name,age)
    
c=child("hina",5)
c.print()

#super() 
class parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
class child(parent):
    def __init__(self,name,age):
        super().__init__(name,age)

c=child("hinata",6)
c.print()

#add properties
class parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
class child(parent):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.year=year #add properties

c=child("j",1,200)
print(c.year)

#add function/method
class parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
class child(parent):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.year=year
    def func(self):
        print(self.name,self.age,self.year)
c=child("j",2,2025)
c.func()

