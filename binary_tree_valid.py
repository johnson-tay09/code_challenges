# Problem Domain: Write a function that takes in a binary tree and verifies if it is a binary search tree or not.

# INPUT: binary tree
# OUTPUT: boolean

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def validate_tree(tree):
    check_false = []

    def walk(node):
        # if not node.left or not node.right:
        #   return None
        if node.left:
            if node.val < node.left.val:
                check_false.append(1)
                # print(is_binary_search_tree)
            walk(node.left)
        if node.right:
            if node.val > node.right.val:
                check_false.append(1)

            walk(node.right)
    walk(root)
    if 1 in check_false:
        return False
    return True


root = Node(10)
root.left = Node(7)
root.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(5)
# root = iter(root)
print(validate_tree(root))
