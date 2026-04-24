# 5.An element is a leader if all elements to its right are smaller.
 
# Example:
# [16,17,4,3,5,2] → leaders: 17, 5, 2

inputs=[16,17,4,3,5,2]

for i in range(len(inputs)-1):
    # print(i)
    if inputs[i]>inputs[i+1]:
        print(inputs[i],end="")