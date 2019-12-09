from num2words import num2words 
from collections import deque

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def leaves(root):
    global result
    if(root.left is None and root.right is None):
        result.append(root.data)
    else:
        if (root.left is not None):
            leaves(root.left)
        if (root.right is not None):
            leaves(root.right)

def boundaryleft(root):
    global result
    if (root):
        result.append(root.data)
        if (root.left is not None):
            boundaryleft(root.left )
        if (root.right is not None):
            leaves(root.right)

def boundaryright(root):
    global result
    if(root):
        if (root.left is not None):
            leaves(root.left )
        if (root.right is not None):
            boundaryright(root.right)
        result.append(root.data)

def boundary(root):
    global result
    if (root):
        result.append(root.data) 
        if (root.left is not None):
            boundaryleft(root.left)
        if (root.right is not None):
            boundaryright(root.right)

def formbinarytree(nodes, index):
    root = Node(nodes.pop(0))
    dq = deque([root])
    while nodes:
        node = dq.popleft()
        temp1 = nodes.pop(0)
        if (temp1 != -1):
            node.left = Node(temp1)
            if (node.left != -1):
                dq.append(node.left)
        if not nodes:
            break
        temp2 = nodes.pop(0)
        if(temp2 != -1):
            node.right = Node(temp2)
            if (node.right != -1):
                dq.append(node.right)
    return root

def inorder(root):
    if (root is not None):
        inorder(root.left)
        print("ordered ",root.data)
        inorder(root.right)

result = []
nodes = []
n = int(input("enter the number of element"))
for i in range(n):
    temp = int(input())
    nodes.append(temp)
#print(nodes)

root = formbinarytree(nodes, 0)

boundary(root)
sum = 0
for i in range(len(result)):
    sum = sum + result[i]
  #  print("boundary ",result[i])

print(num2words(sum))
inorder(root)