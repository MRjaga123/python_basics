# Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Example 1:
# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]Output: 20Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
# Example 2:
# # Input: root = [4,3,null,1,2]Output: 2Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
# Example 3:
# Input: root = [-4,-2,-5]Output: 0Explanation: All values are negatives. Return an empty BST.
# Constraints:
# The number of nodes in the tree is in the range [1, 4 * 104].
# -4 * 104 <= Node.val <= 4 * 104

#############################normal tree
# class normal_tree():
#     def __init__(self,value):
#         self.value=value
#         self.root=[]
#         self.children=[]
#     def add_roots(self,roots):
#         self.root.append(roots)
#     def add_child(self,childs):
#         self.children.append(childs)
#     def __repr__(self):
#         return f"node({self.value})"

# root=normal_tree("A")
# childb=normal_tree("B")
# childc=normal_tree("C")

# root.add_child(childb)
# root.add_child(childc)
# # a.add_child("D")

# final=root.children
# # print(eval(repr(final)))
# print(final)

#############################using trees in python libraries
# # networkx (for graph-like trees)
# # scikit-learn (for decision trees)
# # anytree (for basic tree)
# from anytree import Node,RenderTree

# root=Node("A")

# b=Node("B",parent=root)
# c=Node("C",parent=root)

# print(RenderTree(root))

#############################binary tree
# class binary_tree():
#     def __init__(self,value):
#         self.value=value
#         self.leftchild=None
#         self.rightchild=None
#     def __str__(self):
#         return self.value

# root=binary_tree("A")
# print(root)
# root.leftchild=binary_tree("B")
# print(root.leftchild)
# root.rightchild=binary_tree("C")
# print(root.rightchild)


class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
class solution():
    def __init__(self):
        self.root=None
    def insert(self,root,value):
        if root == None:
            return Node(value)
        if root.left==None:
            root.left=Node(value)
        if root.right==None:
            root.right=Node(value)
        return root
    # def delete(self,root,value):
        # if root == value:
            # return del

# class solution():
#     def __init__(self,roots):
#         self.roots=roots

#     def __repr__(self):
#         return str(self.roots)

array=[1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]
s=solution()
s.insert(s.root,1)
print(s.root.value)
s.insert(s.root,2)
s.insert(s.root,3)
print(s.root.left.value)
