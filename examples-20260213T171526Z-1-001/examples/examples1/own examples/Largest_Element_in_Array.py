# Given an array arr[]. The task is to find the largest element and return it.

# Examples:

# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr[] = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
# Input: arr[] = [10]
# Output: 10
# Explanation: There is only one element which is the largest.

arr=list(map(int,input("arr:").split()))
arr2=0
for i in range(len(arr)):
    # i1=str(i)
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
arr2=(int(arr[-1]))
# print(arr)
print(arr2)
    # print(i)