import tkinter as tk

queue = []


class QueueVisual(tk.Tk):
    def __init__(self, queue):
        super().__init__()
        self.title("Stack Visualization")
        self.geometry("400x400")
        self.queue = queue

        self.input_label = tk.Label(self.master, text="Enter a value:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.master)
        self.input_entry.pack()

        self.append_button = tk.Button(self.master, text="Push", command=self.input)
        self.append_button.pack()

        self.pop_button = tk.Button(self.master, text="Pop", command=self.pop)
        self.pop_button.pack()

        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack()

        self.display_queue()
        self.mainloop()

    def input(self):
        value = self.input_entry.get()
        if value:
            self.queue.insert(len(self.queue), value)
            self.display_queue()

    def pop(self):
        if len(self.queue):
            value = self.queue.pop(0)
            self.display_queue(value)
        else:
            self.display_queue()

    def display_queue(self, value = None):
        self.canvas.delete("all")
        x1 = 20
        y1 = 40
        for i in range(len(self.queue)):
            if i == 0:
                self.canvas.create_rectangle(x1, 40+i*25, x1*4, 40+i*25+15, fill="lightgreen")
            else:
                self.canvas.create_rectangle(x1, 40+i*25, x1*4, 40+i*25+15, fill="cyan")
            self.canvas.create_text(x1+20, 47+i*25, text=str(self.queue[i]))
        if value:
            self.canvas.create_rectangle(x1*4+5, y1, x1*8+5, 65, fill="red")
            self.canvas.create_text(x1*4+25, 25 + 1 * 25, text=str(value))


app = QueueVisual(queue)
