# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # hash table for storing original values
        copy_node = {}
        new_head = Node(head.val)
        copy_node[head] = new_head
        # cursors, like aliases to refer to nodes
        p1 = head
        p2 = new_head
        #scan and copy
        while p1.next is not None:
            p2.next = Node(p1.next.val)
            copy_node[p1.next] = p2.next
            p2 = p2.next
            p1 = p1.next
        p1 = head
        while p1 is not None:
            if p1.random is not None:
                copy_node[p1].random = copy_node[p1.random]
            p1 = p1.next

        return new_head
