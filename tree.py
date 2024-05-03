# Data structure to store a binary tree node
# class Node:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
# def preorderIterative(root):
#     if root is None:
#         return
#     stack = []
#     stack.append(root)
#     curr = root
#     while stack:   # loop till stack is empty
#         if curr:
#             print(curr.data, end=' ')
#             if curr.right:
#                 stack.append(curr.right)
#             curr = curr.left
#         else:
#             curr = stack.pop()
# def recursively_preorder(root):
#     if root is None:
#         return
#     print(root.data,end="")
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)
# preorderIterative(root)



# wap for inorder tre traversal
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#     def insert(self, new_data):
#        if self.data:
#             if new_data < self.data:
#                 if self.left is None:
#                     self.left = Node(new_data)
#                 else:
#                     self.left.insert(new_data)
#             elif new_data > self.data:
#                 if self.right is None:
#                     self.right = Node(new_data)
#                 else:
#                     self.right.insert(new_data)
#        else:
#             self.data = new_data
#     def inorderTraversal(self, root):
#         res = []
#         if root:
#             res = self.inorderTraversal(root.left)
#             res.append(root.data)
#             res = res + self.inorderTraversal(root.right)
#         return res
#
# root = Node(27)
# root.insert(14)
# for i in range(46,65,2):
#     root.insert(i)
# print(root.inorderTraversal(root))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#     def insert(self, data):
#          if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#          else:
#             self.data = data
#
#     def inorderTraversal(root):
#         result = []
#         stack = []
#         current=root
#         while True:
#             if current is not None:
#                 stack.append(current)
#                 current = current.left
#
#             elif (stack):
#                 current = stack.pop()
#                 print(current.data, end=" ")
#                 current = current.right
#             else:
#                 pass
#         return result
#
# root = Node(27)
# root.insert(14)
# for i in range(46,65,2):
#     root.insert(i)
# print(root.inorderTraversal(root))
#

# wap for postorder traversal :-
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def postorderTraversal(root):
#     result = []
#     stack = []
#     if root:
#         stack.append(root)
#     while stack:
#         current = stack.pop()
#         result.append(current.data)
#         if current.left:
#             stack.append(current.left)
#         if current.right:
#             stack.append(current.right)
#     return result
#
# def LevelOrder(root):
#     if root is None:
#         return
#     queue = []
#     queue.append(root)
#     while queue :
#         print(queue[0].data, end=" ")
#         node = queue.pop()
#         if node.left is not None:
#             queue.append(node.left)
#         if node.right is not None:
#             queue.append(node.right)
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# result = postorderTraversal(root)
# LevelOrder(root)
# print(result)

# wap for prinitng the leaf nodes in a tree:-
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def printLeafNodes(root):
#     if (not root):
#         return
#     if (not root.left and not root.right):
#         print(root.data, end=" ")
#         return
#     if root.left:
#         printLeafNodes(root.left)
#     if root.right:
#         printLeafNodes(root.right)
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.right.left = Node(5)
# root.right.right = Node(8)
# root.right.left.left = Node(6)
# root.right.left.right = Node(7)
# root.right.right.left = Node(9)
# root.right.right.right = Node(10)
# printLeafNodes(root)

# wap for finding the ancestor of a given node:-
'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printancestores(root,node):
    if root is None:
        return False
    if root.data==node:
        return True
    if (printancestores(root.left,node) or printancestores(root.data,node)):
        print(root.data,end=",")
        return True
    return False
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(8)
root.right.left.left = Node(6)
root.right.left.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)
num = int(input("Enter the node: "))
print("Ancestors of the node are:" , end="")
printancestores(root,num)'''

# wap for intersting values into binary search tree:-
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Defining a function to insert the given value of x into the tree
# def insert(root, x):
#     if root is None:
#         return Node(x)
#     else:
#         if root.val == x:
#             return root
#         elif root.val < x:
#             root.right = insert(root.right, x)
#         else:
#             root.left = insert(root.left, x)
#     return root
# def inorderTraversal(root):
#     if root:
#         inorderTraversal(root.left)
#         print(root.val, end=" ")
#         inorderTraversal(root.right)
# root = Node(9)
# root.left = Node(1)
# root.right = Node(10)
# root.left.left = Node(0)
# root.left.right = Node(3)
# root.left.right.right = Node(4)
# print("The tree before insertion: ")
# inorderTraversal(root)
# print("\n")
# x = 5
# v = insert(root, x)
# print("The tree after insertion: ")
# inorderTraversal(v)

# iterative solution for insertingin bst:-
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insert(root, x):
    node = Node(x)
    if root is None:
        return Node(x)
    curr = root
    while curr:
        if curr.val == x:
            return root
        if curr.val > x:
            if curr.left:
                curr = curr.left
            else:
                curr.left = node
                break
        if curr.val < x:
            if curr.right:
                curr = curr.right
            else:
                curr.right = node
                break
    return root
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)
root = Node(9)
root.left = Node(1)
root.right = Node(10)
root.left.left = Node(0)
root.left.right = Node(3)
root.left.right.right = Node(4)
print("The tree before insertion: ")
inorderTraversal(root)
print("\n")
x = 5
v = insert(root, x)
print("The tree after insertion: ")
inorderTraversal(v)