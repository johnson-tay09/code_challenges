class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


def rev_linkedList(llist):
    current = llist.head
    if current.next is None:
        llist.head = current
    counter = [0]
    # save head nodes next value
    next_node = current.next
    # if loop hasn't started
    if counter[0] < 1:
        # make the original head the tail
        current.next = None
    # declar prev variable
    prev = None

    def walk(current, next_node, prev):
        while next_node:
            if current.next == None:
                llist.head = current
                current.next = prev
                return
            prev = current
            current = next_node
            next_node = current.next
            counter.append(1)
            walk(current, next_node, prev)
    walk(current, next_node, prev)
    return llist


llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print(rev_linkedList(llist))

# ----------------------------------------------
