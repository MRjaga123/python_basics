#calculator using class,objects and functions:

print("MINI CALCULATOR")
class calculator():
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def add(self):
        print(f"add={self.num1 + self.num2}")

    def sub(self):
        print(f"sub={self.num1 - self.num2}")

    def mul(self):
        print(f"mul={self.num1 * self.num2}")

    def div(self):
        print(f"div={self.num1 / self.num2}")

c=calculator(a=int(input("enter a:")),b=int(input("enter b:")))
c.add()
c.sub()
c.mul()
c.div()

