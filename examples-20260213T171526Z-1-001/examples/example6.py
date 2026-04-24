#array sorting without sort method

x=int(input("enter the number:"))
a=[]

for i in range(x):
    x=[]
    y=int(input("enter the numbers:"))
    x.append(y)
    a.append(x)
print(a)

for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>=a[j]:
            q=a[i]
            a[i]=a[j]
            a[j]=q
print(a)