from tkinter import *
import tkinter as tk
from tkinter import messagebox
from queue1 import Queue
from stack import Stack
from sllist import SingleLinkedList
from dllist import DoublyLinkedList


class DataTypesVisualiser:
    def __init__(self, master):
        self.master = master
        self.master.title("Queue Visualizer")
        self.queue = Queue()

        self.input_label = tk.Label(self.master, text="Enter a value:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.master)
        self.input_entry.pack()

        self.enqueue_button = tk.Button(self.master, text="Enqueue", command=self.enqueue_value)
        self.enqueue_button.pack()

        self.dequeue_button = tk.Button(self.master, text="Dequeue", command=self.dequeue_value)
        self.dequeue_button.pack()

        self.queue_display = tk.Label(self.master, text="Queue: ")
        self.queue_display.pack()

        self.display_queue()
        print(self.queue)

    def enqueue_value(self):
        value = self.input_entry.get()
        if value:
            self.queue.push(23)
            self.display_queue()
        else:
            messagebox.showwarning("Input Error", "Please enter a value")

    def dequeue_value(self):
        if self.queue:
            self.queue.popleft()
            self.display_queue()
        else:
            messagebox.showinfo("Queue Empty", "The queue is already empty")

    def display_queue(self):
        self.queue_display.config(text="Queue: " + str(self.queue.toString))


if __name__ == "__main__":
    root = tk.Tk()
    app = DataTypesVisualiser(root)
    root.mainloop()
