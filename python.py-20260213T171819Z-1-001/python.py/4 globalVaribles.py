#global variable

x="jaga"
def myFunc():
    print("x="+x)
myFunc()

y="zoro"
def myfunc():
    y="jaga"
    print("y="+y)

myfunc()
print("y="+y)


#global keyword
x = "jaga"

def func():
  global x
  x = "zoro"

func()
print("x=" + x)