#matrix sorting

import numpy

x=int(input("enter the row:"))
y=int(input("enter the col:"))
a=[]

for i in range(x):
    for j in range(y):
        z=numpy.array(int(input(f"enter the element[{i}][{j}]:")))
        a.append(z)
a=numpy.sort(a,axis=None).reshape(x,y)
print(a)
        
        
   