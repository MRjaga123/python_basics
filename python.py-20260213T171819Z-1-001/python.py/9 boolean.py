#python boolean
print(10>9)
print(10==9)
print(10<9)

#boolean in if statement
a=4
a1=5
if a>a1:
    print("a is greater")
else:
    print("a1 is greater")

#evaluate values and variables
b="jaga"
b1=15
b2=None
b3=0
b4=""
print(bool(b))
print(bool(b1))
print(bool(b2))
print(bool(b3))
print(bool(b4))

print("")
#boolean retun false in class
class jaga():
    def __len__(self):
        return 0
j=jaga()
print(bool(j))

#function return boolean 
def func():
    return True
print(func())

def funcc():
    return False
print(funcc())

#if statement to check boolean
def funccc():
    return True
if funccc():
    print("yes")
else:
    print("no")

#use isinstance() function to check datatype by boolean 
c=300
print(isinstance(c,int))
c1="300"
print(isinstance(c1,int))

