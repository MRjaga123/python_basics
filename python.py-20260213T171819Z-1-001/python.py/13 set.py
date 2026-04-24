#set{}     #unordered #unchangeable #unindexed #donot allow duplicate value #store any data type

myset={"jaga","zoro","zoya","hinata"}
print(myset)
print(type(myset))

myset={"jaga",1,True,False,0,34}          #store any data type
print(myset)

#length of set
myset={"jaga","zoro","zoya","hinata"}
print(len(myset))

#set() constructor
myset=set(("jaga","zoro","zoya","hinata"))
print(myset)
print(type(myset))

#access set items
myset={"jaga","zoro","zoya","hinata"}

for i in myset:               #loop in set
    print(i)

myset={"jaga","zoro","zoya","hinata"}
print("jaga" in myset)        #check in set
myset={"jaga","zoro","zoya","hinata"}
print("jaga" not in myset)

##add set items
#add() method
myset={"jaga","zoro","zoya","hinata"}
myset.add("hina")
print(myset)

#update() method 
myset={"jaga","zoro","zoya","hinata"}  #add two sets
myset1={"jaga","zoro","hema","hina"}
myset.update(myset1)
print(myset)

#add any iterable
myset={"jaga","zoro","zoya","hinata"} 
mylist=["j","z","z","h"]
mytuple=("ja","zo","zo","hi")

myset.update(mylist)
print(myset)
myset.update(mytuple)
print(myset)

##remove set items

myset={"jaga","zoro","zoya","hinata"}
myset.remove("jaga")            #remove() method 
print(myset)
myset.discard("hina")           #discard() method
print(myset)

myset={"jaga","zoro","zoya","hinata"}
myset.clear()                   #clear the set
print(myset) 

myset={"jaga","zoro","zoya","hinata"}
del myset                       #delete the set

######################################################join sets
#union() method
set1={"jaga","hina",1}
set2={"hina","zoro",2}
set3={"zoya",3,4}

set4=set1.union(set2,set3)
set5=set1|set2|set3

print(set4)
print(set5)

set1={"jaga","zoro"}  #set join with other datatype
list=["zoya","hina"]
set=set1.union(list)
print(set)

#intersection() method
set1={"jaga","hina",1}
set2={"hina","zoro",2}
set3={"zoya",3,4,"hina"}

set4=set1.intersection(set2,set3)
set5=set1&set2&set3

print(set4)
print(set5)

set1={"jaga","hina"}
list=["jaga",1]
set=set1.intersection(list) #set join with other datatype
print(set)

#difference() method
set1={"jaga","hina",1}
set2={"jaga","zoro",2}
set3={"hina","zoro",3}

set4=set1.difference(set2,set3)
set5=set1-set2-set3

print(set4)
print(set5)

set1={"jaga",1,2}
list=["jaga",2,4]
set=set1.difference(list) #set join with other datatype
print(set)

#symmetric difference
set1={"jaga","hina",1}
set2={"hina","zoro",2}

set4=set1.symmetric_difference(set2)
set5=set1^set2

print(set4)
print(set5)

set1={"jaga","zoya","hina"}
list=["jaga",1,2]
set=set1.symmetric_difference(list)#set join with other datatype
print(set)

