from problems.bonusproblem.Node import Node
import tkinter as tk


class TreePlot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Plot")
        self.window.geometry("1800x900")
        self.canvas = tk.Canvas(self.window, width=1800, height=900, bg="white")
        self.texts = []
        self.canvas.pack()

    @staticmethod
    def calculate_x(i, subtrees, parent_x, level):
        if subtrees % 2 != 0 and (subtrees // 2) == i:
            return parent_x
        level_factor = 1.5
        x_offset_left_start = parent_x - (600 / ((level + 1) * level_factor))
        x_offset_right_end = parent_x + (600 / ((level + 1) * level_factor))
        space = x_offset_right_end - x_offset_left_start
        rel_position = (i / (subtrees - 1)) * space  # - 1
        return x_offset_left_start + rel_position

    def add_reason_text(self, position_x, x, position_y, y, child):
        x_begin = (position_x + x) / 2
        y_begin = (position_y + y) / 2
        self.canvas.create_rectangle(x_begin - 30, y_begin - 10, x_begin + 50, y_begin + 10, fill="white", width=0)
        content = f"{child.reason[child.reason.index(':') + 1:].strip()}"
        t_id = self.canvas.create_text(x_begin, y_begin,
                                       text=content,
                                       fill="black", font=("Helvetica", 12))
        self.texts.append(t_id)

    def texts_to_front(self, texts):
        for t in texts:
            self.canvas.tag_raise(t)

    def plot(self, tree: Node, x=900, y=50, level=0, goal=""):
        for i in range(len(tree.children)):
            position_x = self.calculate_x(i, len(tree.children), x, level)
            position_y = y + 100
            self.canvas.create_line(x, y, position_x, position_y, fill="blue", width=2)
            self.add_reason_text(position_x, x, position_y, y, tree.children[i])
            self.plot(tree.children[i], position_x, position_y, level + 1)

        self.canvas.create_rectangle(x - 50, y - 10, x + 50, y + 10, fill="white", width=0)
        t_id = self.canvas.create_text(x, y, text=f"{tree.data}", fill="black", font=("Helvetica", 12))
        self.texts.append(t_id)
        if level > 0:
            return
        self.canvas.create_text(x, 20, text=f"Goal: {goal}", fill="black", font=("Helvetica", 18))
        self.texts_to_front(self.texts)
        self.window.mainloop()
