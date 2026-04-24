#data structures and algorithms

###datastructures

##############################list and array
x=[]
y=[1,2,3,4,5]
z=[1,"jaga",True,1.4]

x.append(8)
x.append(7)
x.sort()
print(x)

#creating algorithms
#find lowest value
my_array=[3,4,5,2,1]
min=my_array[0]
for i in my_array:
    if i<min:
        min=i
print("min:",min)

##############################stacks-LIFO
stack=[]

#push
stack.append(1)
stack.append(5)
stack.append(2)
stack.append(4)
stack.append(3)
print("stack push:",stack)

#peek
topElement=stack[-1]
print("topElement peek:",topElement)

#pop
popElement=stack.pop()
print("popElement pop:",popElement)
print(stack)#after pop

#isEmpty
isEmpty=not(stack)
print("isEmpty:",isEmpty)

#size
print("size:",len(stack))

#creating stack using class
class stack():
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    
    def isEmpty(self):
        self.isEmpty==0

    def size(self):
        if self.isEmpty():
            return "stack is empty"
        return len(self.stack)

s=stack()
s.push(3)
s.push(2)
s.push(1)

print("stack:",s.stack)
print("peek:",s.peek())
print("pop:",s.pop())
print("size:",s.size())
print("stack:",s.stack)



##############################queues-FIFO
queue=[]

#enqueue
queue.append(1)
queue.append(4)
queue.append(2)
queue.append(3)
print("queue:",queue)

#peek
topElement=queue[0]
print("peek:",topElement)

#dequeue
dequeue=queue.pop(0)
print("dequeue:",dequeue)

#isEmpty
isEmpty=not (queue)
print("isEmpty:",isEmpty)

#size
size=len(queue)
print("size:",size)


#creating queue using class
class queue():
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,element):
        self.queue.append(element)

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.queue[0]

    def dequeue(self):
        if self.isEmpty():
            return "stack is empty"
        return self.queue.pop(0)

    def isEmpty(self):
        self.isEmpty==0

    def size(self):
        if self.isEmpty():
            return "stack is empty"
        return len(self.queue)    
q=queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)

print("queue:",q.queue)
print("peek:",q.peek())
print("dequeue:",q.dequeue())
print("size:",q.size())


##############################linked list
##############################hash table
##############################trees
##############################graphs

###algorithms

#linear algorithm
#binary algorithm
#selection sort
#insertion sort
#quick sort
#merge sort
#bubble sort
#counting sort
#radix sort
