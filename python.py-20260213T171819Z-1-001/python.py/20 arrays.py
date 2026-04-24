


#arrays

name=["jaga","zoya","zoro","hina","hinata","naruto","sasuke","sanji"] #array
print(name)

x=name[0]        #acess the array
print(x)

name[0]="nobita"  #change the array
print(name)

print(len(name)) #length of array

for i in name:   #loop of array
    print(i)

name.append("jaga") #append() for add
print(name)

name.pop(8)      #pop() for remove by index
print(name)

name.remove("sanji") #remove() for remove by value
print(name)

name.clear()      #clear array
print(name)  

name=["jaga","zoya","zoro","hina","hinata","naruto","sasuke","sanji"]
print(name)

name1=name.copy() #copy() for copy the array
print(name1)

print(name.count("jaga"))  #count in array

name=["jaga","zoya","zoro","hina","hinata","naruto","sasuke","sanji"]
name1=["jaga","zoya","zoro","hina","hinata","naruto","sasuke","sanji"]

name.extend(name1)                                   #extend the one array with another array         
print(name)

print(name.index("zoro"))   #find the index number

name.insert(0,"nobita")    #insert the value in array
print(name)

name.sort()  #sort the array
print(name)

name.reverse() #reverse the array
print(name)