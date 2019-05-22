class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkList:
    def __init__(self):
        self.head = Node(None)

    def init_list(self, target_list):
        node = self.head
        for i in target_list:
            node.next = Node(i)
            node = node.next

    def show(self):
        node = self.head.next
        while node != None:
            print(node.value, end=' ')
            node = node.next

    def append(self, value):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def get_length(self):
        count = 0
        node = self.head
        while node.next is not None:
            node = node.next
            count += 1
        return count

    def is_empty(self):
        if self.head.next == None:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None

    def get_item(self,index):
        node = self.head.next
        count = 0
        while node.next is not None:
            if count == index:
                return node.value
            node = node.next
            count+=1



link_list = [1, 2, 3, 5, 8, 10]
l = LinkList()
l.init_list(link_list)
l.append(5)
l.show()
print("=========================")
print(l.get_item(2))

