import math
import time
from tkinter import messagebox
from tkinter import *
import tkinter as tk

import timer


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.selected = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.selected = new_node
            return 0
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.selected = new_node
            return self.find(self.selected)

    def remove(self):
        if self.head == self.selected:
            current = self.head
            while current.next != self.selected:
                current = current.next
            if self.head == self.head.next:
                self.head = None
                self.selected = None
            else:
                self.head = self.head.next
                current.next = self.head
                self.selected = current
        else:
            current = self.head
            while current.next != self.selected:
                current = current.next
            current.next = self.selected.next
            self.selected = current
        return self.find(self.selected)

    """
    def remove(self, key):
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                self.head = self.head.next
                current.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next
    """

    def selectNext(self):
        self.selected = self.selected.next
        return self.find(self.selected)

    def find(self, element):
        if self.head is None:
            return None
        num = 0
        current = self.head
        while True:
            if current == element:
                return num
            else:
                current = current.next
                num += 1
            if current == self.head:
                break
        return num

    def display(self):
        elements = []
        temp = self.head
        if temp:
            while True:
                elements.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        print(elements)


class CircularListVisualization(tk.Tk):
    def __init__(self, circular_linked_list):
        super().__init__()
        self.title("Circular Linked List Visualization")
        self.geometry("400x400")
        self.circular_linked_list = circular_linked_list

        self.input_label = tk.Label(self.master, text="Enter a value:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.master)
        self.input_entry.pack()

        self.append_button = tk.Button(self.master, text="Append", command=self.input)
        self.append_button.pack()

        self.delete_label = tk.Label(self.master, text="Selector")
        self.delete_label.pack()

        self.select_button = tk.Button(self.master, text="Next", command=self.next)
        self.select_button.pack()

        self.delete_button = tk.Button(self.master, text="Remove", command=self.delete)
        self.delete_button.pack()

        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack()

        self.display_list()
        self.mainloop()

    def input(self):
        value = self.input_entry.get()
        if value:
            num = self.circular_linked_list.append(value)
            self.display_list(num)

    def next(self):
        current = self.circular_linked_list.selected
        if current is not None:
            self.display_list(self.circular_linked_list.selectNext())

    def delete(self):
        # value = self.delete_entry.get()
        # if value:
        try:
            next = self.circular_linked_list.remove()
            self.display_list(next)
        except Exception as ass:
            messagebox.showwarning(str(ass))

    def display_list(self, selected=None):
        self.canvas.delete("all")
        elements = []
        temp = self.circular_linked_list.head
        if selected is None:
            selected = 0
        while True:
            if temp:
                elements.append(temp.data)
                temp = temp.next
            if temp == self.circular_linked_list.head:
                break

        if len(elements):
            radius = 100
            angle = 360 / len(elements)
            x1 = 0
            y1 = 0
            xi = 0
            yi = 0
            for i, data in enumerate(elements):
                x = 150 + radius * math.sin(math.radians(angle * i))
                y = 150 + radius * math.cos(math.radians(angle * i))
                if selected == i:
                    self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red")
                    self.canvas.create_text(self.canvas.winfo_x(), 15, text="data: " + (str(data)))
                else:
                    self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="lightgreen")
                    self.canvas.update()
                    self.canvas.after(200)
                    self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="cyan")
                self.canvas.create_text(x, y, text=str(data))
                if (i == 0):
                    x1, xi = x, x
                    y1, yi = y, y
                else:
                    self.draw_arrow(xi, yi, x, y)
                xi = x
                yi = y
            self.draw_arrow(xi, yi, x1, y1)

    def draw_arrow(self, x1, y1, x2, y2):
        arrow_length = 7
        # Нарисовать линию
        line = self.canvas.create_line(x1, y1, x2, y2)
        # Нарисовать треугольник в конце линии
        angle = math.atan2(y2 - y1, x2 - x1)
        x3 = x2 - arrow_length * math.cos(angle - math.pi / 6)
        y3 = y2 - arrow_length * math.sin(angle - math.pi / 6)
        x4 = x2 - arrow_length * math.cos(angle + math.pi / 6)
        y4 = y2 - arrow_length * math.sin(angle + math.pi / 6)
        self.canvas.create_polygon(x2, y2, x3, y3, x4, y4)


circular_list = CircularLinkedList()
app = CircularListVisualization(circular_list)
