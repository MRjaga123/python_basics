#if elif else statement

#logical conditions
a=5
b=10

a==b #equal to
a!=b #not equal to
a<b  #less than
a<=b #less than or equal
a>b  #greater than
a>=b #greatet than or equal

#if
a=10
b=20
if a<b:
    print("a is big")

#if elif
a=10
b=10
if a<b:
    print("a is bid")
elif a==b:
    print("a and b are equal")

#if elif else
a=20
b=10
if a<b:
    print("a is big")
elif a==b:
    print("a and b are equal")
else :
    print("b is big")

#short hand if else
a=10
b=20

print("a") if a>b else print("equal") if a==b else print("b")

###logical operators and logical conditions
#and
a=10
b=20
c=30
if a<b and a<c:
    print("print both conditions is true")
#or
a=10
b=20
c=30
if a<b or a>c:
    print("print if one condition is true")
#not
a=10
b=20
if not a>b:
    print("a is not big")

#nested if
x=30

if x>40:
    print("x is big")
if x<40:
        print("x is small")
else:
        print("x")
#Pass                     
x=30

if x>40:
    pass


