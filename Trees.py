class Node:
    def __init__(self, data):
        self.data = data
        self.left:Node = None
        self.right:Node = None


node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4

node3.left = node5
node3.right = node6

def find_sum(root):
    if root == None:
        return 0
    return root.data + find_sum(root.left) + find_sum(root.right)

print(find_sum(node2))
