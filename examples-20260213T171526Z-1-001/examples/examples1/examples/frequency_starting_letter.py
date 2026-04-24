# 7.Build Frequency Dictionary of Words Per Starting Letter
# Count how many words start with each alphabet.
 
# Input:
# ["cat","car","dog","doll","apple"]
 
# Output:
# {"c":2,"d":2,"a":1}

inputs=["cat","car","dog","doll","apple"]
frequency={}

for i in inputs:
    # print(i)
    for j in i[0]:
        if j in frequency:
            frequency[j]+=1
        if j not in frequency:
            frequency[j]=1
print(frequency)
