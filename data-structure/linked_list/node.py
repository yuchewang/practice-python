class LinkedListNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return "(" + str(self.data) + ")"