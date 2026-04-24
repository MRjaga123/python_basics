#iterators
#__iter__() and __next__() 

#iter and next
mylist=["jaga","zoya","zoro"]
myiter=iter(mylist)

print(next(myiter))
print(next(myiter))
print(next(myiter))

mystr="jagadeesh"
myiter=iter(mystr)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#loop actually works as iterator
for i in mystr:
    print(i)

#create an iterator
class number():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x
    
n=number()
myiter=iter(n)

print(next(myiter))
print(next(myiter))
print(next(myiter))

#
class number():
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration

n=number()
myiter=iter(n)

print(next(myiter))

for i in myiter:
    print(i)
    
