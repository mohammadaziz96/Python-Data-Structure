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
        return node
t=Tree()
root=t.CreateNode(int(input("Enter root node: ")))
print(root.data)
print(type(root.data))
t.insert(root, int(input("Enter element to insert: ")))
t.insert(root, int(input("Enter element to insert: ")))
t.insert(root, int(input("Enter element to insert: ")))
t.insert(root, int(input("Enter element to insert: ")))
t.insert(root, int(input("Enter element to insert: ")))
