#while loops

i=0
while i<6:
    print(i)
    i=i+1

print("break")
#break statement
i=0
while i<6:
    print(i)
    if i==4:
        break
    i=i+1
    

print("continue")
#continue statement
i=0
while i<6:
    i=i+1
    if i==4:
        continue
    print(i)
    
print("else")
#else statement
i=0
while i<=6:
    print(i)
    i=i+1
else:
    print("i")