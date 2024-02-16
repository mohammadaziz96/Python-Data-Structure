#Create binary tree and insert few element.
class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data
class Tree:
    def CreateNode(self, data):
        return Node(data)
    def insert(self, node, data):
        if node is None:
            return self.CreateNode(data)
        if data>=node.data:
            node.right=self.insert(node.right, data)
        else:
            node.left=self.insert(node.left, data)
        return Node
t=Tree()
root=t.CreateNode(10)
print(root.data)
print(type(root.data))
print("Enter 5 element on each input")
t.insert(root, int(input("Enter element: ")))
t.insert(root, int(input("Enter element: ")))
t.insert(root, int(input("Enter element: ")))
t.insert(root, int(input("Enter element: ")))
t.insert(root, int(input("Enter element: ")))
