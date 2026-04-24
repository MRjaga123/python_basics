#matrix sorting without sort method

rows=int(input("enter the rows:"))
cols=int(input("enter the cols:"))
a=[]

for i in range(rows):
    rows=[]
    for j in range(cols):
        z=int(input("enter the numbers:"))
        rows.append(z)
    a.append(rows)
print(a)

flat=[]
for i in range(0,len(rows)):
    for j in range(0,cols):
        flat.append(a[i][j])
print(flat)

for i in range(0,len(flat)):
    for j in range(i,len(flat)):
        if flat[i]>=flat[j]:
            q=flat[i]
            flat[i]=flat[j]
            flat[j]=q
print(flat)

k=0
for i in range(0,len(rows)):
    for j in range(cols):
        a[i][j]=flat[k]
        k+=1
print(k)
print(flat)

for i in a:
    print(i)

