#user inputs

name=input("enter your name:")
print(f"hello {name:}")

#multiple inputs
name=input("enter your name:")
print(f"hello {name:}")

age=int(input("enter your age:"))
bike=str(input("enter your bike:"))
print("age:",age)
print("bike:",bike)

#validate input
x=bool(input("enter true or false:"))
while x==True:
    name=str(input("name:"))
    number=int(input("number:"))
    try:
        name=str(name);
        number=int(number);
        x=False
    except:
        print("something wrong")
print("tq")
