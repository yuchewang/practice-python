from node import LinkedListNode

class CircularLinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def add(self,data):
        new_node = LinkedListNode(data)
        if self.size == 0:
            self.root = new_node
            self.root.next = self.root
        else:
            new_node.next = self.root.next
            self.root.next = new_node
        self.size += 1

    def find(self,data):
        cur = self.root
        while True:
            if cur.data == data:
                return data 
            elif cur.next == self.root:
                return False
            cur = cur.next
            
        return None

    def remove(self,data):
        cur = self.root
        prev = None
        while True:
            if cur.data == data:
                if prev is not None:
                    prev.next = cur.next
                else:
                    while cur.next != self.root:
                        cur = cur.next
                    cur.next = self.root.next
                    self.root = self.root.next
                self.size-=1
                return True
            elif cur.next == self.root:
                return False
            prev = cur
            cur = cur.next


    def print_list(self):
        if self.root is None:
            return
        cur = self.root
        print(cur , end="->")
        while cur.next != self.root:
            cur = cur.next
            print(cur , end="->")
        print()

if __name__ == "__main__":
    l = CircularLinkedList()
    l.add(5)
    l.print_list()
    l.add(6)
    l.print_list()
    l.add(8)
    l.add(12)
    l.print_list()

    print("size:" + str(l.size))
    l.remove(8)
    l.print_list()
    print("size:" + str(l.size))
    l.print_list()
    print(l.find(5))
    print(l.root)