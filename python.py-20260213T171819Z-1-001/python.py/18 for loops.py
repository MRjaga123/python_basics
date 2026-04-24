#for loops

forloop="jaga"
for i in forloop:
    print(i)

forlooplist=["for","loop","list"]         #for loop in list
for i in forlooplist:
    print(i)

forlooptuple=("for","loop","tuple")       #for loop in tuple
for i in forlooptuple:
    print(i)

forloopset={"for","loop","set"}           #for loop in set
for i in forloopset:
    print(i)

forloopdict={"name":"jaga","age":21}      #for loop in dict
for i in forloopdict.items():
    print(i)

print("break")
#break statement
x="jaga"
for i in x:
    if i=="g":
        break
    print(i)

x=["j","a","g","a"]
for i in x:
    if i =="a":
        break
    print(i)

print("continue")
#continue statement
x="jaga"
for i in x:
    if i=="g":
        continue
    print(i)

x=["j","a","g","a"]
for i in x:
    if i=="g":
        continue
    print(i)

print("else")
#else statement
x=[1,2,3,4,5]
for i in x:
    if i==4:
        break
    print(i)
else:
    print("end")

for i in range(0,10,2):
    if i==8:
        break
    print(i)
else:
    print("end")


print("range")
#range() funtion
for i in range(6):
    print(i)

for i in range(3,6):
    print(i)

for i in range(1,20,5):
    print(i)


print("nested loop")
#nested loops
x=["j","a","g","a"]
y=[1,2,3,4,]

for i in x:
    print("")
    for j in y:
        print("*",x,y)

for i in range(3):    #pass
    pass

#
count=0
for i in range(1,10):
    if i % 2 ==0:
        print(i)
        count+=1
print(f"we have {count} even numbers")