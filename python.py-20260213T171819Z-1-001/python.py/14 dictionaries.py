#dictionaries{key:value}  #store str,int,boolean and list datatypes 
                            #ordered #changeable #no duplicate value

mydict={"name":"jaga","age":21}
print(mydict)
print(type(mydict))
print(mydict["name"])
print(len(mydict))

mydict={
    "name":"jaga",  #str
    "age":21,       #int
    "yes":True,     #boolean
    "bike":["zoro","zoya"]  #list
}
print(mydict)

#dict() constructor
mydict=dict(name="jaga",age=21)   
print(mydict)

#access items
mydict={
    "name":"jaga",  
    "age":21,       
    "yes":True,     
    "bike":["zoro","zoya"]  
}

print(mydict["yes"])        
print(mydict.get("age"))    #get
print(mydict.keys())        #keys
print(mydict.values())      #values
print(mydict.items())       #items

mydict["no"]=False #join
mydict["age"]=20   #change
mydict.update({"name":"hina"})  #update()
print(mydict)

#check
mydict={
    "name":"jaga",  #str
    "age":21,       #int
    "yes":True,     #boolean
    "bike":["zoro","zoya"]  #list
}
if "name" in mydict:
    print("yes")

#remove
mydict={
    "name":"jaga",  
    "age":21,      
    "yes":True,     
    "bike":["zoro","zoya"]  
}
mydict.pop("yes")  #pop()
print(mydict)
mydict.popitem()   #popitem()
print(mydict)
del mydict["age"]  #del
print(mydict)
mydict.clear()     #clear()
print(mydict)

#loop
mydict={
    "name":"jaga",  
    "age":21,      
    "yes":True,     
    "bike":["zoro","zoya"]  
}
for i in mydict:              #loop for key
    print(i)
for i in mydict:              #loop for value
    print(mydict[i])

for i in mydict.keys():       #loop for keys
    print(i)

for i in mydict.values():     #loop for values
    print(i)

for i in mydict.items():      #loop for items
    print(i)

#copy dictionary
mydict={
    "name":"jaga",  
    "age":21,      
    "yes":True,     
    "bike":["zoro","zoya"]  
}
mydict1=mydict.copy()
print(mydict1)

#nested dictionaries
jaga1={
     "child1":{
     "name":"j",
     "year":2003},
     "child2":{
     "name":"a",
     "year":2004},
     "child3":{
     "name":"g",
     "year":2005}
}
print(jaga1)

#or
child1={
     "name":"j",
     "year":2003}
child2={
     "name":"a",
     "year":2004}
child3={
     "name":"g",
     "year":2005}
myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(myfamily)

print(myfamily["child1"]["name"])  #access items in nested loop

#loop in nested loop
for x,y in myfamily.items():
    print(x,y)

