#scope

#1 local scope
def func():
    x=10
    print(x)
func()

def func1(): #func inside func
    x=10
    def func2():
        print(x)
    func2()
func1()

#2 global scope
x=30
def func():
    print(x)
func()
print(x)

#naming variables
x=40
def func():
    x=50
    print(x)
func()
print(x)

#3 global keyword
x=60
def func():
    global x
    x=70
func()
print(x)

#4 nonlocal keyword
def func1():
    x=80
    def func2():
        nonlocal x
        x=100
    func2()
    return x
print(func1())
