##################datetime

import datetime
x=datetime.datetime.now()
print(x)

print(x.day)
print(x.month)
print(x.year)
print(x.second)
print(x.minute)
print(x.hour)

#strftime()method
import datetime
x=datetime.datetime.now()

print(x.strftime("%A"))
print(x.strftime("%a"))

print(x.strftime("%B"))
print(x.strftime("%b"))



#create date
import datetime
x=datetime.datetime(2003,11,28)
print(x)


###################### math
import math

#min/max()
x=min(10,5,1)
y=max(10,5,1)
print("min:",x)
print("max:",y)

#abs()
x=abs(-7.2)
print("abs:",x)

#pow()
x=2
y=3
print("power:",pow(x,y))

#sprt()
x=math.sqrt(4)
print("square reote:",x)

#ceil/floor()
x=math.ceil(1.5)
y=math.floor(1.5)
print("ceil:",x)
print("floor:",y)

#pi
x=math.pi
print(x)