import tkinter as tk

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.selected = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.selected = new_node



    def delete(self):
        current = self.head
        while current:
            if current.next == self.selected:
                if current.next.next is not None:
                    current.next = current.next.next
                    self.selected = current.next
                else:
                    current.next = None
                    self.selected = self.head
                return
            current = current.next


class DoublyLinkedListVisualizer:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=400)
        self.canvas.pack()
        self.linked_list = DoublyLinkedList()
        self.node_positions = {}

    def draw_list(self, selected = None):
        self.canvas.delete("all")
        current = self.linked_list.head
        afterfill = "lightblue"
        x = 50
        while current:
            if current == selected:
                afterfill = "red"
            else:
                afterfill = "lightblue"
            self.node_positions[current.data] = (x, 200)
            self.canvas.create_oval(x-20, 180, x+20, 220, fill='lightgreen')
            self.canvas.create_text(x, 200, text=str(current.data))
            self.canvas.update()
            self.canvas.after(100)
            if current != self.linked_list.head:
                self.canvas.create_line(x-50, 200, x-20, 200, arrow=tk.LAST)
            self.canvas.create_oval(x - 20, 180, x + 20, 220, fill=afterfill)
            self.canvas.create_text(x, 200, text=str(current.data))
            x += 100
            current = current.next

    def add_node(self):
        data = int(self.entry.get())
        self.linked_list.insert(data)
        self.draw_list(self.linked_list.selected)

    def delete_node(self):
        self.linked_list.delete()
        self.draw_list(self.linked_list.selected)

    def create_interface(self):
        self.entry = tk.Entry(self.master)
        self.entry.pack()

        add_button = tk.Button(self.master, text="Add Node", command=self.add_node)
        add_button.pack()

        delete_button = tk.Button(self.master, text="Delete Node", command=self.delete_node)
        delete_button.pack()

        next_button = tk.Button(self.master, text="Next", command=self.next)
        next_button.pack()


    def next(self):
        if self.linked_list.selected.next:
            self.linked_list.selected = self.linked_list.selected.next
        else:
            self.linked_list.selected = self.linked_list.head
        self.draw_list(self.linked_list.selected)


root = tk.Tk()
doubly_linked_list_visualizer = DoublyLinkedListVisualizer(root)
doubly_linked_list_visualizer.create_interface()
doubly_linked_list_visualizer.draw_list()
root.mainloop()