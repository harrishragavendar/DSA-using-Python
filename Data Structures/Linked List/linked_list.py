class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, val):
        node = Node(val, next_node=self.head)
        self.head = node

    def __str__(self):
        curr = self.head
        node_vals = []
        while curr:
            node_vals.append(curr.val)
            curr = curr.next
        if len(node_vals) > 0:
            return ' -> '.join(map(str, node_vals))
        else:
            return '[]'

ll = LinkedList()
print(ll)

for i in range(1, 6):
    ll.insert_first(i)

print(ll)