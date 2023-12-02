class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, node: Node):
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if node.data < current.data:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = node
                        break
                else:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = node
                        break
    
    def displayTree_BFS(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)


tree = BinaryTree()
tree.addNode(Node(5))
tree.addNode(Node(3))
tree.addNode(Node(7))
tree.addNode(Node(2))
tree.addNode(Node(4))
tree.addNode(Node(6))
tree.addNode(Node(8))

tree.displayTree_BFS()

# assignment
#Implement displayTree_DFS
# pros and cons of DFS and BFS
