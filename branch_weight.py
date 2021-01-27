

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def check_weight(root, n):
    target = n
    total_so_far = 0
    match_found = []

    def traverse_add(node, total_so_far):
        total_so_far += node.val
        if node.left:
            traverse_add(node.left, total_so_far)
        if node.right:
            traverse_add(node.right, total_so_far)
        if not node.left and not node.right:
            # print(total_so_far)
            if target == total_so_far:
                match_found.append(1)

    traverse_add(root, total_so_far)
    if 1 in match_found:
        return True
    return False


# Driver code
root = Node(10)
root.left = Node(7)
root.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(5)

print(check_weight(root, 20))
