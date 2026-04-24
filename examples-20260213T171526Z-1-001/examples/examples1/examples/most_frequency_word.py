# 6.Find the Most Frequent Word (Ignore Case & Punctuation)
# Problem:
# Given a sentence, return the word with the highest frequency.
 
# Input:
# "Apple banana apple fruit Banana apple!!!"
 
# Output:
# apple

inputs="Apple banana apple fruit Banana apple!!!"
frequency={}

for i in inputs.lower().replace("!","").split(" "):
    if i in frequency:
        frequency[i]+=1
    if i not in frequency:
        frequency[i]=1
print(frequency)

inputs1=[i for i in frequency.keys()]
print(inputs1[0])

# for i in inputs1:
#     print(i[0])
