#arithmetic operator
print(5+5) #add(+)
print(5-5) #sub(-)
print(5*5) #mult(*)
print(5/5) #div(/)
print(5%10) #modulus(%)
print(5**2) #exponentiation(**)
print(5//5) #floor div(//)

print("")
#assignment operator
x=5            # =
print(x)       
x+=3           # +=
print(x)
x-=3           # -=
print(x)
x*=3           # *=
print(x)
x/=3           # /=
print(x)

x=5
x%=3           # %=
print(x)

x=5
x//=3          # //=
print(x)

x=5
x**=3           # **=
print(x)

print("")
#comparison operator
x=5
y=10

print(x==y)  #equal to
print(x!=y)  #not equal to
print(x<y)   #less than
print(x>y)   #greater than
print(x<=y)  #less than or equal to
print(x>=y)  #greater than or equal to

print("")
#logical operator
x=5

print(x<9 and x>4)  #and
print(x>4 or x<3)   #or
print(not(x>3))     #not

print("")
#identify operator
x="jaga"
y="jaga"

print(x is y)          # is
print(x is not y)      # is not

x=["jaga","zoro"]
y=["jaga","zoro"]
z=x

print(x is y)          #is
print(x is not y)      #is not
print(x is z)

print("")
#membership operator
x=["jaga","zoro"]
print("jaga" in x)     # in
print("zoro" not in x) # not in

print("")
#bitwise operator
print(6 & 3)           # & and
print(6 | 3)           #| or
print(6 ^ 3)           #^ xor
print(~ 6)             #~ not
print(3 << 2)          #left shift
print(8 >> 2)          #right shift



#precedence describes the order which operation performs firts
#()
#**
#etccc...



