#matrix:get row and column inputs from user ,if user give 3:3 means ,print 3x3 martrix

x=int(input("enter the row:"))
y=int(input("enter the column:"))

a=[]
for i in range(x):
    x=[]

    for j in range(y):
        z=int(input("enter the no:"))
        x.append(z)

    a.append(x)
for i in a:
    print(i)    

print(a)
