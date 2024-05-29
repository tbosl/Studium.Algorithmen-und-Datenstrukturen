import math

from problems.bonusproblem.Node import Node
import tkinter as tk


def calculate_offset(level, origin):
    if level == 0:
        return origin / (level + 0.8)
    else:
        return origin / (level + 1.5)


def calculate_x(i, subtrees, parent_x, level):
    if subtrees % 2 == 1 and subtrees // 2 == i:
        return parent_x
    denominator = subtrees // 2
    offset = calculate_offset(level, 450)
    if i < subtrees // 2:
        numerator = denominator - i
        scale = numerator / denominator
        return parent_x - (scale * offset)
    else:
        start = i + 1 if subtrees % 2 == 0 else i
        numerator = start - denominator
        scale = numerator / denominator
        return parent_x + (scale * offset)


class TreePlot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Plot")
        self.window.geometry("1800x900")
        self.canvas = tk.Canvas(self.window, width=1800, height=900, bg="white")
        self.texts = []
        self.canvas.pack()

    def __add_rectangle(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", width=0)

    def __add_text(self, x, y, content):
        self.texts.append(self.canvas.create_text(x, y,
                                                  text=content,
                                                  fill="black", font=("Helvetica", 12)))

    def add_reason_text(self, position_x, x, position_y, y, child):
        x_begin = (position_x + x) / 2
        y_begin = (position_y + y) / 2
        self.__add_rectangle(x_begin - 30, y_begin - 10, x_begin + 50, y_begin + 10)
        self.__add_text(x_begin, y_begin, f"{child.reason[child.reason.index(':') + 1:].strip()}")

    def texts_to_front(self, texts):
        for t in texts:
            self.canvas.tag_raise(t)

    def __root_jobs(self, x, goal):
        self.canvas.create_text(x, 20, text=f"Goal: {goal}", fill="black", font=("Helvetica", 18))
        self.texts_to_front(self.texts)
        self.window.mainloop()

    def __plot_node(self, x, y, tree):
        self.canvas.create_rectangle(x - 50, y - 10, x + 50, y + 10, fill="white", width=0)
        self.__add_text(x, y, f"{tree.data}")

    def plot(self, tree: Node, x=900, y=50, level=0, goal=""):
        for i in range(len(tree.children)):
            position_x = calculate_x(i, len(tree.children), x, level)
            position_y = y + int((200 / (level + 1)))
            self.canvas.create_line(x, y, position_x, position_y, fill="blue", width=2)
            self.add_reason_text(position_x, x, position_y, y, tree.children[i])
            self.plot(tree.children[i], position_x, position_y, level + 1)

        self.__plot_node(x, y, tree)
        if level == 0:
            self.__root_jobs(x, goal)
