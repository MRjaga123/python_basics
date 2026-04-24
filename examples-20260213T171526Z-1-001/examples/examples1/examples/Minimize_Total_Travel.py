# Batch Optimization: Minimize Total Travel
# 1 elevator starting at floor 5.
# You get a batch of pickup requests:
# (2→8)
# (9→3)
# (4→10)
# You must order pickups to minimize travel.
# Test Input
# 5
# 3
# 2   8
# 9   3
# 4   10
# Expected Output (one optimal order)
# 4→10
# 2→8
# 9→3
# Reason
# Sorted by nearest source to current floor (5):

# Request	Distance
# 4→10	    1
# 2→8	    3
# 9→3	    4

def Minimize_total_Travel(inputs):
    source=test_input[0]
    # print(source)
    output=[]
    output1=[]
    output2=[]
    for i in inputs:
        i1=str(i)
        # print(i)
        if i==source:
            output.append(source)
        else:
            if [i1][0]!=i1[-1]:
                # a=sorted(i1[0])  
                output1.append(i)
            elif [i1][0]==i1[-1]:
                output2.append(i)
                # print(output2)
    # print(output2)
    print(output1)
    print(output)
    output3={}
    for j in output1:
        if j[0] and j[1]:
            # print(j[0],j[1])
            if j[0]:
                output3[j]=abs(j[0]-source)
    print(output3)
    output4=[]
    for k in output3.items():
        output4.append(k)
    print(output4)

    for m in range(len(output4)):
        for n in range(m+1,len(output4)):
            if output4[m][1]>output4[n][1]:
                output4[m],output4[n]=output4[n],output4[m]
    print(output4)

    for l in output4:
        print(l[0])
    # print(sorted(output3))
            # pass
    
test_input=[5,3,(2,8),(9,3),(4,10)]
# source=test_input[0]
# print(source)

Minimize_total_Travel(test_input)
