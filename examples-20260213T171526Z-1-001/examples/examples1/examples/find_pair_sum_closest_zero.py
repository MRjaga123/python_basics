# 4.Given a list of integers, find the pair whose sum is closest to zero.
# example:
# [1, 60, -10, 70, -80, 85] → [-80, 85] (sum = 5)

inputs=[1,60,-10,70,-80,85]
inputs1={}

for i in range(0,len(inputs),2):
    # if inputs[i] and inputs[i+1]:
    if inputs[i] and inputs[i+1]:
        a=inputs[i]+inputs[i+1]
        inputs1[inputs[i],inputs[i+1]]=a
print(inputs1)

inputs[:]=[i for i in inputs1.items()]
print(inputs)

for i in range(len(inputs)):
    for j in range(i+1,len(inputs)):
        if inputs[i][1]>inputs[j][1]:
            inputs[i],inputs[j]=inputs[j],inputs[i]
print(inputs[0])
