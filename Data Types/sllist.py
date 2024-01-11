class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def pushBack(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def pushForward(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def popForward(self):
        if self.isEmpty():
            raise Exception("List is empty")
        value = self.head.value
        self.head = self.head.next
        return value



