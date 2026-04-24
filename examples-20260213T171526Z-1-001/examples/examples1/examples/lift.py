# Problem 4 — Assign Request to Lift with Minimum Arrival Time
# Lifts:
# A at 2 → stops ahead = [6, 9]
# B at 7 → stops ahead = []
# New request: source=4
# Time cost formula:
# Travel time = |current_floor - source| + pending_stops_count
# Test Input
# 2 A 2 2 6 9 B 7 0 4
# Explanation
# Lift A: distance = |2-4| = 2, pending = 2 → cost = 4
# Lift B: distance = |7-4| = 3, pending = 0 → cost = 3
# Expected Output
# Lift B assigned (cost=3)

def cost(lift,source,stops):
    distance=abs(lift-source)
    pending=stops
    return distance+pending

lifts=[2,"A",2,2,6,9,"B",7,0,4]

index_A=lifts.index("A")#1
current_index_A=lifts[index_A+1]
pending_index_A=lifts[index_A+2]
# print(index_A)
# print(current_index_A)
# print(pending_index_A)

index_B=lifts.index("B")#7>>b
current_index_B=lifts[index_B+1]#8>>7
pending_index_B=lifts[index_B+2]
# print(index_B)
# print(current_index_B)
# print(pending_index_B)

sources=lifts[-1]#9
# print(sources)

a=cost(current_index_A,sources,pending_index_A)
print(a)
b=cost(current_index_B,sources,pending_index_B)
# print(a)
print(b)

# if a<b:
#         print(f"Lift B assigned (cost={a})")
#         # Lift B assigned (cost=3)
# if b<a:
#         print(f"Lift A assigned (cost={b})")
# else:
#         print("equal")
