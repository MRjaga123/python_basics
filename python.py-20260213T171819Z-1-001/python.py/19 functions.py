#functions >> def

def myfunc():     #function
    print("jaga")
myfunc()          #calling the function

#arguments
def myfunc(name):
    print(name)
myfunc("zoya")

def myfunc(name="jaga"): #default arguments
    print(name)
myfunc("zoro")
myfunc()

def myfunc(name,age):   #numbers of arguments
    print(name,age)
myfunc("zora",21)
myfunc("hina",21)

def myfunc(*name):      #arbitrary arguments,*args
    print(name[1])
myfunc("jaga","zoya")

def myfunc(**name):     #keyword arbitrary arguments,**kwargs
    print(name["a"])
myfunc(a="hina",b="hinata")

def myfunc(a,b,c):      #keyword arguments
    print(b)
myfunc(a="jaga",b="zzzz",c="zoro")

#passing list as an arguments
def myfunc(name):
    print(name)

mylist=["jaga","zoyz","zoro"]
myfunc(mylist)

#return values
def myfunc(x):
    return 3*x
print(myfunc(3))

#pass statement
def myfunc():
    pass

#combine position only(/,) and keyword only(*,)
def myfunc(a,/,*,b,c):
    print(a+b+c)
myfunc(1,b=1,c=1)

#recursion
def factorial(n):  #factorial
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def fibonacci(n):  #fibonacci
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(6))

######################lambda function
x=lambda a,b:a+b
print(x(1,1))

x=lambda a,b,c:a*b*c
print(x(1,1,1))

#lambda function inside a function
def myfunc(x):
    return lambda y:y*x
a=myfunc(5)
print(a(5))

def func(x):
    return lambda y:y*x
a=func(2)
b=func(3)

print(a(11))
print(b(11))
