#stacks and queues
#stack-lifo
class stacks():
    def __init__(self):
        self.stack=[]

    #push
    def push(self,element):
        self.stack.append(element)
  

    #isempty
    def isempty(self):
        self.isempty==0

    #peek
    def peek(self):
        if self.isempty():
            return "stsck is empty"
        return self.stack[-1]
    
    #pop
    def pop(self):
        if self.isempty():
            return "stack is empty"
        return self.stack.pop(-1)
    
    #size
    def size(self):
        if self.isempty():
            return "stck is empty"
        return len(self.stack)
    
    #display
    def display(self):
        print(self.stack)

s=stacks()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.isempty())
print(s.peek())
print(s.pop())
print(s.size())
print(s.display())

    
#queue-fifo
class queues():
    def __init__(self):
        self.queue=[]

    #push
    def push(self,element):
        self.queue.append(element)

    #is empty
    def isempty(self):
        self.isempty == 0
        
    #peek 
    def peek(self):
        if self.isempty():
            return "queue is empty"
        return self.queue[0]

    #pop
    def pop(self):
        if self.isempty():
            return "queue is empty"
        return self.queue.pop(0)

    #size
    def size(self):
        if self.isempty():
            return "queue is empty"
        return len(self.queue) 

    #display
    def display(self):
        print(self.queue)      
    
q=queues()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

print(q.isempty())
print(q.peek())
print(q.pop())
print(q.size())
print(q.display())

