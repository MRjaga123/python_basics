#OOP
#polymorphism #multiple classes have same name fuctions

class car():
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def move(self):
        print("drive")

class boat():
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def move(self):
        print("sail")

class plane():
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def move(self):
        print("fly")

c1=car("honda",2000)
b1=boat("yamaha",2001)
p1=plane("airbus",2002)

c1.move()

for i in (c1,b1,p1):
    i.move()


print("")
#inheritance in polymorphism
class vehicle():
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def move(self):
        print("move")

class car(vehicle): #inherits
    pass
   
class boat(vehicle):#inherits
    def move(self):  #poly
        print("sail")

class plane(vehicle):#inherits
    def move(self):#poly
        print("fly")

c1=car("honda",2000)
b1=boat("yamaha",2001)
p1=plane("airbus",2002)

for i in (c1,b1,p1):
    print(i.brand)
    print(i.year)
    i.move()

##encapsulation
##abstraction
