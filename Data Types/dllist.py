import tkinter as tk

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def visualize_deletion_traversal(self, data):
        current = self.head
        while current:
            if current.data == data:
                current.is_current = True  # Отметить текущий элемент
            else:
                current.is_current = False
            current = current.next

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                self.visualize_deletion_traversal(data)  # Визуализация перебора
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
class DoublyLinkedListVisualizer:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=400)
        self.canvas.pack()
        self.linked_list = DoublyLinkedList()
        self.node_positions = {}

    def draw_list(self):
        self.canvas.delete("all")
        current = self.linked_list.head
        x = 50
        while current:
            self.node_positions[current.data] = (x, 200)
            self.canvas.create_oval(x-20, 180, x+20, 220, fill='lightblue')
            self.canvas.create_text(x, 200, text=str(current.data))
            if current.prev:
                self.canvas.create_line(x-50, 200, x-20, 200, arrow=tk.LAST)
            if current.next:
                self.canvas.create_line(x+20, 200, x+50, 200, arrow=tk.LAST)
            x += 100
            current = current.next

    def highlight_node(self, data, color):
        x, y = self.node_positions[data]
        self.canvas.create_oval(x-20, 180, x+20, 220, fill=color)
        self.canvas.create_text(x, 200, text=str(data))

    def add_node(self):
        data = int(self.entry.get())
        self.linked_list.insert(data)
        self.draw_list()

    def delete_node(self):
        data = int(self.entry.get())
        self.linked_list.delete(data)
        self.draw_list()

    def highlight_cycle(self):
        current = self.linked_list.head
        while current:
            self.highlight_node(current.data, 'lightgreen')
            self.master.update()
            self.master.after(200)  # Ждем 1 секунду
            self.highlight_node(current.data, 'lightblue')
            current = current.next
            if current == self.linked_list.head:  # Выход из цикла, если вернулись к началу
                break

    def create_interface(self):
        self.entry = tk.Entry(self.master)
        self.entry.pack()

        add_button = tk.Button(self.master, text="Add Node", command=self.add_node)
        add_button.pack()

        delete_button = tk.Button(self.master, text="Delete Node", command=self.delete_node)
        delete_button.pack()

        cycle_button = tk.Button(self.master, text="Highlight Cycle", command=self.highlight_cycle)
        cycle_button.pack()

root = tk.Tk()
doubly_linked_list_visualizer = DoublyLinkedListVisualizer(root)
doubly_linked_list_visualizer.create_interface()
doubly_linked_list_visualizer.draw_list()
root.mainloop()