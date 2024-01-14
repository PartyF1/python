from tkinter import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListGUI:
    def __init__(self, master):
        # Инициализация списка
        self.head = None
        self.tail = None

        # Создание виджетов
        frame = Frame(master)
        frame.pack()

        self.entry = Entry(frame)
        self.entry.pack(side=LEFT)

        add_button = Button(frame, text="Add", command=self.add)
        add_button.pack(side=LEFT)

        del_button = Button(frame, text="Delete", command=self.del_node)
        del_button.pack(side=LEFT)

    def add(self):
        val = self.entry.get()
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.tail
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = new_node
            new_node.next = self.tail







root = Tk()
LinkedListGUI(root)
root.mainloop()