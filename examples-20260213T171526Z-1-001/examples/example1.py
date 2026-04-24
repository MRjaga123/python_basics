#get input from user ,if user give 3 means ,and then get 3 inputs from user ,finally display it

a=[]
enter=int(input("enter your number:"))
for i in range(1,enter+1):
    x=int(input(i))
    if x%2!=0:
        a.append(x)
    else:
        print("enter another number:")
        x=int(input(i))
        print(x)
        a.append(x)
print(a)

