from node import LinkedListNode

class SingleLinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    
    def add(self,data):
        new_node = LinkedListNode(data, self.root)
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
        prev = None
        while cur is not None:
            if cur.data == data:
                if prev is not None:
                    prev.next = cur.next
                else:
                    self.root = cur.next

                self.size-=1
                return True
            else:
                prev = cur
                cur = cur.next
        return False

    def reverse(self):
        if self.root == None: 
            return
        prev = None
        cur = self.root
        post = self.root.next
        while post != None:
            cur.next = prev
            prev = cur
            cur = post
            post = post.next
        cur.next = prev
        self.root = cur

    def print_list(self):
        cur = self.root
        while cur is not None:
            print(cur , end="->")
            cur = cur.next
        print('None')


if __name__ == "__main__":
    l = SingleLinkedList()
    l.add(5)
    l.add(6)
    l.add(8)
    l.add(12)
    l.print_list()
    l.reverse()
    l.print_list()

    print("size:" + str(l.size))
    l.remove(8)
    print("size:" + str(l.size))
    print(l.find(5))
    print(l.root)