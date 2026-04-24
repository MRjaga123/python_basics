# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]Output: [1,1,2,3,4,4,5,6]Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:
# Input: lists = []Output: []
# Example 3:
# Input: lists = [[]]Output: []
# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

def linkedlist(L):
    lists1=[]
    for i in L:
        for j in i:
            lists1.append(j)
    # print(lists1)
    for i in range(len(lists1)):
        for j in range(i+1,len(lists1)):
            if lists1[i]>lists1[j]:
                lists1[i],lists1[j]=lists1[j],lists1[i]
    print(lists1)
    # pass

lists=[[1,4,5],[1,3,4],[2,6]]
# lists=[[]]
linkedlist(lists)
