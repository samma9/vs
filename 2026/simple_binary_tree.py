# Simple Binary Tree PF 6.8
# Samuel Marriott 8/03/2026

class Node:
    def __init__(self, value):
        self.value = value  # Stores the value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# Creates the root node and child nodes
root = Node(42)
root.left = Node(56)
root.right = Node(13)

# Further connects child nodes to the root and its children
root.left.left = Node(21)
root.left.right = Node(8)
root.right.right = Node(72)

# Define the preorder_traversal() function
def preorder_traversal(node):
    if node:
        print(node.value, end = " ")  # Print the current node's value
        preorder_traversal(node.left)  # Traverse the left child
        preorder_traversal(node.right)  # Traverse the right child

print("Preorder Traversal: ")
preorder_traversal(root)

# Define the inorder_traversal() function
def inorder_traversal(node):
    if node:  # Check if the current node exists
        inorder_traversal(node.left)  # Traverse the left child
        print(node.value, end = " ")  # Print the current node's value
        inorder_traversal(node.right)  # Traverse the right child

print("\n Inorder Traversal:")
inorder_traversal(root)