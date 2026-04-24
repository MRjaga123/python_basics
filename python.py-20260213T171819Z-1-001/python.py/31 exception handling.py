#############exception handling
#try
#except
#else
#finally

#
try:
    print(x)
except:
    print("error")

#
try:
    print(x)
except NameError:
    print("name error")
except:
    print("something wrong")

#
try:
    print("hello")
except:
    print("error")
else:
    print("no error")

#
try:
    print(x)
except:
    print("error")
else:
    print("no error")
finally:
    print("finally finished")

#
try:
    x=open(jaga.py)
    try:
        write.x("jaga")
    except:
        print("write error")
except:
    print("open error")

#raise keyword
x=-1
if x<0:
    raise Exception("sorry for the error")
