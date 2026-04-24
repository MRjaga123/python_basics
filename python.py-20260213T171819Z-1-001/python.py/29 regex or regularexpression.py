#RegEx >>Regular Expression ##used for search pattern

import re


text="hi, i am jaga"
#search
x=re.search("i*am",text)
print(x)

if x:
    print("match")
else:
    print("no match")

#findall()
y=re.findall("i",text)
print(y)

#split()
z=re.split("\s",text)
print(z)

#sub()
a=re.sub("\s","1",text)
print(a)



