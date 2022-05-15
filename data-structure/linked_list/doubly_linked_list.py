from node import LinkedListNode

class DoublyLinkedList:
    def __init__(self, root = None):
        self.root = root
        self.last = root
        self.size = 0
    
    def add(self,data):
        # only when there's nothing in the list should we change the last pointer
        if self.size == 0:
            self.root = LinkedListNode(data, self.root)
            self.last = self.root
        else:
            new_node = LinkedListNode(data, self.root)
            self.root.prev = new_node
            self.root = new_node
        self.size += 1

    def find(self,data):
        cur = self.root
        while cur is not None:
            if cur.data == data:
                return data
            else:
                cur = cur.next
        return None

    def remove(self,data):
        cur = self.root
        while cur is not None:
            if cur.data == data:
                if cur.prev is not None:
                    if cur.next is not None: # delete middle node
                        cur.next.prev = cur.prev
                        cur.prev.next = cur.next
                    else: # delete last node
                        self.last = cur.prev
                        self.last.next = None
                else: # delete root node
                    self.root = cur.next
                    self.root.prev = None
                self.size-=1
                return True
            else:
                cur = cur.next
        return False

    def print_list(self):
        cur = self.root
        while cur is not None:
            print(cur , end="->")
            cur = cur.next
        print('None')


if __name__ == "__main__":
    dll = DoublyLinkedList()
    for i in [1,2,3,4,5,6,7,8,9]:
        dll.add(i)
    
    print("size:" + str(dll.size))

    dll.print_list()
    dll.remove(7)
    print("size:" + str(dll.size))
    dll.print_list()
