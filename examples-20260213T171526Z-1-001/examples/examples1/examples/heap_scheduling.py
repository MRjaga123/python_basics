# Problem 3 — Two-Heap Scheduling (Up/Down Stops)
# Lift is currently at floor 4 and moving up.
# Up-heap = min-heap, Down-heap = max-heap.
# Incoming stops:
# 7, 2, 9, 5, 1
# Test Input
# 4 up
# 7 2 9 5 1
# Expected Processing Order
# Up requests → floors > 4
# Down requests → floors < 4
# Up-heap: 5, 7, 9
# Down-heap: 2, 1
# Since direction = up:
# 5 7 9 # direction switch 2 1
# Expected Output
# 5 7 9 2 1

# import heapq
# heap=[]
# print("empty heap:",heap)

# heapq.heappush(heap,7)
# heapq.heappush(heap,2)
# heapq.heappush(heap,9)
# heapq.heappush(heap,5)
# heapq.heappush(heap,1)
# print("pushed heap:",heap)

# heapq.heappop(heap)
# print("pop heap(smallest):",heap)

# a=[7, 2, 9, 5, 1]
# heapq.heapify(a)
# print(a)


from collections import deque

a=[7, 2, 9, 5, 1]
inputs=input("enter 'up' or 'down': ")

b=deque()
c=deque()

for i in a:
    if i>4:
        b.appendleft(i)
    elif i<4:
        c.append(i)

b=sorted(b)
c=sorted(c,reverse=True)

a.clear()
match inputs.lower():
    case "up":
        print(b+c)
    case "down":
        print(c+b)
    case _:
        print("error")
# a=b+c
# print(b)
# print(c)
# print(a)

