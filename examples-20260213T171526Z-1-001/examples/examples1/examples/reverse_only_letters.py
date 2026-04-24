# 3.Reverse Only Letters (Keep Digits Same Position)
# Reverse only letters in the string.
# Do NOT move digits.
# Example:
# Input: "a1b2c3d"
# Output: "d1c2b3a"
# Explanation:
# Letters: a,b,c,d → reversed to d,c,b,a
# Digits stay at the same index.

inputs ="a1b2c3d"

inputs1=[]
for i in inputs:
    if i.isalpha():
        inputs1.append(i)
inputs1.sort(reverse=True)
# print(inputs1)

result=[]
indexs=0
for i in inputs:
    if i.isalpha():
        result.append(inputs1[indexs])
        indexs+=1
    else:
        result.append(i)
print("".join(result))




# inputs1[:]=("".join(sorted(inputs1,reverse=True)))
# print(inputs1)

# for i in range(len(inputs)-1):
#     # print(i)
#     if inputs[i].isalpha():
#         if inputs[i]<inputs[i+1]:
#             inputs[i],inputs[i+1]=inputs[i+1],inputs[i]
