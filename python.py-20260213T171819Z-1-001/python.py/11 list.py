#list []  #ordered #changeable #allow duplicate #store any data type

mylist=["jaga","zoro","zoya","hinata"]

print(mylist)
print(mylist[0])

list1=["jaga","zoro"]     #list can be any data type
list2=[2,3,5,8,1]
list3=[True,False,True]
list4=["jaga",2,3,False]

print(len(mylist))        #length of list

print(type(mylist))       #find type
print(type(list4)) 

#list constructor
mylist=list(("jaga","zoro"))
print(mylist)
print(type(mylist))

#access the list items
mylist=["jaga","zoro","zoya","hinata"]

print(mylist[0])   #index
print(mylist[-1])  #negative index

print(mylist[1:3]) #range of index
print(mylist[:2])
print(mylist[2:])

print(mylist[-2:-1]) #range of negative index

#check the item is exists on list
mylist=["jaga","zoro","zoya","hina"]
if "jaga" in mylist:
    print("yes")
else:
    print("no")

#change list items
mylist=["jaga","zoro","zoya","hinata"]
mylist[1]="hina"
print(mylist)

mylist[1:3]=["zr","zy"] #change range of list items
print(mylist)

#insert() method
mylist=["jaga","zoro","zoya","hinata"]
mylist.insert(3,"hina")
print(mylist)

#append() method 
mylist=["jaga","zoro","zoya","hinata"]
mylist.append("hina")
print(mylist)

#extend() method
mylist1=["jaga","zoro"]
mylist2=["zoya","hinata"]
mylist1.extend(mylist2)
print(mylist1)
print(mylist2)

#remove() method
mylist=["jaga","zoro","zoya","hinata"]
mylist.remove("jaga")
print(mylist)

#pop() method
mylist=["jaga","zoro","zoya","hinata"]
mylist.pop(-1)
print(mylist)

mylist=["jaga","zoro","zoya","hinata"]
mylist.pop()
print(mylist)

#del method
mylist=["jaga","zoro","zoya","hinata"]
del mylist[1]
print(mylist)

mylist=["jaga","zoro","zoya","hinata"]
del mylist                                    #full list is deleted

#clear() method
mylist=["jaga","zoro","zoya","hinata"]
mylist.clear()
print(mylist)                                 #clear only content


#loop list

#for loop
mylist=["jaga","zoro","zoya","hinata"]
for i in mylist:
    print(i)
#for loop len() and range()
mylist=["jaga","zoro","zoya","hinata"]
for i in range(len(mylist)):
    print(mylist[i])

#while loop
mylist=["jaga","zoro","zoya","hinata"]
i=0
while i< len(mylist):
    print(mylist[i])
    i=i+1

#Looping Using List Comprehension
mylist=["jaga","zoro","zoya"]
[print(i) for i in mylist]

print("")
#list comprehension
mylist=["jaga","zoro","zoya","hinata"]
newlist=[i for i in mylist if "a" in i]
print(mylist)
print(newlist)

newlist=[i for i in mylist]
print(newlist)

newlist=[i for i in mylist if i != "jaga"]
print(newlist)

newlist=[i if i != "jaga" else "jogo" for i in mylist]
print(newlist)

#list sort #sort()
mylist=["jaga","zoro","zoya","hinata"]
mylist.sort()
print(mylist)

mylist=[1,9,8,2,3,7,4,5,6,5]
mylist.sort()
print(mylist)

mylist=["jaga","zoro","zoya","hinata"]  #sort reverse order
mylist.sort(reverse=True)
print(mylist)

mylist=[1,0,2,9,3,8,4,7,5,6]
mylist.sort(reverse=True)
print(mylist)

#sort function
def func(n):
    return abs(n-10)
mylist=[5,4,6,7,8,9]
mylist.sort(key=func)
print(mylist)

mylist=["jaga","zoro","zoya","hinata"]  #reverse order
mylist.reverse()
print(mylist)

#copy list
mylist=["jaga","hinata"]    
mylist1=mylist
print(mylist1)

mylist=["hinata"]
mylist1=list(mylist)    #list method
print(mylist1)

mylist=["jaga","zoro","zoya","hinata"]
mylist1=mylist.copy()                        #copy() method
print(mylist1)

mylist=["jaga","zoro","zoya","hinata"]
mylist1=mylist[:]                             #slice method for copy
print(mylist1)

#join list
mylist=["jaga","zoro","zoya","hinata"]
mylist1=[1,2,3,4,5]

print(mylist + mylist1)                    # using + operator for join list

mylist=["jaga","zoro","zoya","hinata"]
mylist1=[1,2,3,4,5]

mylist.append(mylist1)                     # usind append() for join list
print(mylist)

mylist=["jaga","zoro","zoya","hinata"]
mylist1=[1,2,3,4,5]

mylist.extend(mylist1)                     #using extend() for join the list
print(mylist)

