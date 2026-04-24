#tuple()         #ordered #unchangeable #allow duplicate #store any data type

mytuple=("jaga","zoro","zoya","hinata")
print(mytuple)
print(mytuple[0])

mytuple1=("jaga","zoro")         #tuple cane be any data type
mytuple2=(1,2,3,4,5)
mytuple3=(True,False)
mytuple4=("jaga",1,True)

print(len(mytuple))            #length of tuple

#create tuple with one item
mytuple=("jaga",)
print(mytuple)
print(type(mytuple))

#tuple() constructor
mytuple=tuple(("jaga","zoro","zoya","hinata"))
print(mytuple)
print(type(mytuple))

#access the tuple
mytuple=("jaga","zoro","zoya","hinata")

print(mytuple[0])            #by index
print(mytuple[-1])           #by negative index

print(mytuple[0:2])          #by range
print(mytuple[:1])
print(mytuple[2:])

print(mytuple[-3:-1])        #by negative range
print(mytuple[:-2])
print(mytuple[-2:])

#check if item exists in tuple
mytuple=("jaga","zoro","zoya","hinata")
if "jaga" in mytuple:
    print("yes")
else:
    print("no")


#update tuple

#change value
x=("jaga","zoro","zoya","hinata")
y=list(x)
y[3]="hina"
x=tuple(y)
print(x)
print(type(x))

#add value
x=("jaga","zoro","zoya","hinata")
y=list(x)
y.append("hina")
x=tuple(y)
print(x)
print(type(x))

#add tuple to tuple
mytuple=("jaga","zoro","zoya","hinata")
mytuple1=("hina",)
mytuple += mytuple1
print(mytuple)

#remove tuple item
x=("jaga","zoro","zoya","hinata")
y=list(x)
y.remove("jaga")
x=tuple(y)
print(x)

#del
mytuple=("jaga","zoro","zoya","hinata")
del mytuple                                  #delete the entire tuple

print("")
#unpack tuples
mytuple=("jaga","zoro","zoya","hinata")

(me,*bike,anime)=mytuple                              # *asterisk

print(me)
print(bike)
print(anime)

#for loop 
mytuple=("jaga","zoro","zoya","hinata")
for i in mytuple:
    print(i)

#for loop len() and range()
mytuple=("jaga","zoro","zoya","hinata")
for i in range(len(mytuple)):
    print(mytuple[i])

#while loop
mytuple=("jaga","zoro","zoya","hinata")
i=0
while i<len(mytuple):
    print(mytuple[i])
    i=i+1

#join tuples
mytuple=("jaga","zoro","zoya","hinata")
mytuple1=("hina",)

mytuple2=mytuple + mytuple1
print(mytuple2)

mytuple2=mytuple * 2
print(mytuple2)

#tuple methods
mytuple=("jaga","zoro","zoya","hinata")
x=mytuple.count("jaga")                   #count
print(x)

y=mytuple.index("zoya")                   #index
print(y)







