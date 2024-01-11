class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


    def pop(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    @property
    def toString(self):
        temp = ""
        if self.head is not None:
            node = self.head
            for i in range(0, self.size):
                node = node.next
                temp.join(" ,").join(str(node))
        return temp