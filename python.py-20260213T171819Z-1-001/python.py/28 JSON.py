#JSON for data storing and data exchange

import json

#convert from json to python
x='{"name":"jaga","age":21}' #some json

y=json.loads(x)
print(y["age"])
print(y["name"])

#convert from python to json
x={"name":"jaga1","age":20}

y=json.dumps(x)
print(y)

#
x={
    "name":"jaga",
   "age":21,
   "single":True,
   "married":False,
   "childre":None,
   "bike":("zoro","zoya"),
   "anime":["naturo","one piece"]
   }
y=json.dumps(x)
print(y)

z=json.dumps(x,indent=3)
print(z)

a=json.dumps(x,indent=4,separators=(".","="))
print(a)

b=json.dumps(x,indent=0,separators=(".","="),sort_keys=True) #order the result
print(b)