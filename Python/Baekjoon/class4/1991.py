import sys
input = sys.stdin.readline
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def print_preorder_traversal(self):
        stack = [self.root]
        while stack:
            current = stack.pop()
            print(current.item, end="")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
    def print_inorder_traversal(self, n):
        if n.left:
            self.print_inorder_traversal(n.left)
        print(n.item, end="")
        if n.right:
            self.print_inorder_traversal(n.right)
    def print_postorder_traversal(self, n):
        if n.left:
            self.print_postorder_traversal(n.left)
        if n.right:
            self.print_postorder_traversal(n.right)
        print(n.item, end="")

N = int(input())
nodes = {}
binary_tree = BinaryTree()
for _ in range(N):
    alphabet, left_alphabet, right_alphabet = input().rstrip().split()
    if alphabet in nodes:
        pass
    else:
        nodes[alphabet] = Node(alphabet)
    if alphabet == "A":
        binary_tree.root = nodes[alphabet]
    if left_alphabet != ".":
        if left_alphabet not in nodes:
            nodes[left_alphabet] = Node(left_alphabet)
        nodes[alphabet].left = nodes[left_alphabet]
    if right_alphabet != ".":
        if right_alphabet not in nodes:
            nodes[right_alphabet] = Node(right_alphabet)
        nodes[alphabet].right = nodes[right_alphabet]
binary_tree.print_preorder_traversal()
print()
binary_tree.print_inorder_traversal(binary_tree.root)
print()
binary_tree.print_postorder_traversal(binary_tree.root)
