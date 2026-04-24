"""romen numbers to normal numbers"""
# Input: s = "III"Output: 3Explanation: III = 3.

dicts={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
total=0#1>4,
total1=0
# dicts1=[]
# dicts2={}

inputs1="IVX"#1994

for i in range(len(inputs1)):
    if total>0:
        if inputs1[i-1]=="I" and (inputs1[i]=="V" or inputs1[i]=="X"):
            t = abs(dicts[inputs1[i-1]] - dicts[inputs1[i]])
            total += t
            total -= dicts[inputs1[i-1]]
        elif inputs1[i-1]=="X" and (inputs1[i]=="L" or inputs1[i]=="C"):
            t = abs(dicts[inputs1[i-1]] - dicts[inputs1[i]])
            total += t
            total -= dicts[inputs1[i-1]]
        elif inputs1[i-1]=="C" and (inputs1[i]=="D" or inputs1[i]=="M"):
            t = abs(dicts[inputs1[i-1]] - dicts[inputs1[i]])
            total += t
            total -= dicts[inputs1[i-1]]
        
        else:
            total += dicts[inputs1[i]]
    else:
        total += dicts[inputs1[i]]
print(total)


# for i in range(len(inputs1)):
#     # print(i)
#     inputs=inputs1.upper()
#     if total >0:
#         if inputs[i-1]=="I" and (inputs[i]=="V" or inputs[i]=="X"):#i>1 and v>5
#             s=abs(dicts[inputs[i-1]]-dicts[inputs[i]])#4
#             total-=dicts[inputs[i-1]]
#             total+=s
#         elif inputs[i-1]=="X" and (inputs[i]=="L" or inputs[i]=="C"):
#             s=abs(dicts[inputs[i-1]]-dicts[inputs[i]])
#             total-=dicts[inputs[i-1]]
#             total+=s
#         elif inputs[i-1]=="C" and (inputs[i]=="D" or inputs[i]=="M"):
#             s=abs(dicts[inputs[i-1]]-dicts[inputs[i]])
#             total-=dicts[inputs[i-1]]
#             total+=s
#         else:
#             total+=dicts[inputs[i]]
#     else:
#         total+=dicts[inputs[i]]
# print(total)



# for i in inputs:
#     # print(i)
#     if i in dicts:
#         # print("yes")
#     # else:
#     #     print("no")
#         for j,k in dicts.items():
#             if i==j:
#                 # print(i,j,k)
#                 dicts2[i]=k
#                 # print("yes")
#                 a=(k)
#                 dicts1.append(a)
# print(dicts1)
# for n in dicts1:
#     # print(n)
#     n1=str(n)
#     n2=[]
#     for m in n1:
#         if n[0]<m[0]
# print(dicts1)
# # print(dicts2)

# for i in inputs:
#     # print(i)
#     if i in dicts:
#         # print("yes")
#     # else:
#     #     print("no")
#         for j,k in dicts.items():
#             if i==j:
#                 # print("yes")
#                 a=(k)
#                 dicts1.append(a)
# print(sum(dicts1))

# for i in inputs:
#     # print(i)
#     if i in dicts:
#         # print("yes")
#     # else:
#     #     print("no")
#         for j,k in dicts.items():
#             if i==j:
#                 dicts2[i]=k
#                 # print("yes")
#                 a=(k)
#                 dicts1.append(a)
# print(sum(dicts1))
# print(dicts2)
