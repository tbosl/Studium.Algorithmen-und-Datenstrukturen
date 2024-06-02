import tkinter as tk

from problems.bonusproblem.Node import Node


def calculate_maximum_offset_for_both_sides(level, original):
    """The function will provide the maximum offset of both tree sides
     based on the current level and the original offset."""
    if level == 0:
        return original / (level + 0.8)
    else:
        return original / (level + 1.5)


def calculate_new_x(i, subtrees, parent_x, level):
    """Use this function to determine the currently selected
      child's x position based on the index, the number of
      subtrees, the parent x coordinate and the level."""
    if subtrees % 2 == 1 and subtrees // 2 == i:
        return parent_x
    children_per_side = subtrees // 2
    offset = calculate_maximum_offset_for_both_sides(level, 450)
    if i < subtrees // 2:
        numerator = children_per_side - i
        scale = numerator / children_per_side
        return parent_x - (scale * offset)
    else:
        index_of_child_in_current_tree_half = i + 1 if subtrees % 2 == 0 else i
        numerator = index_of_child_in_current_tree_half - children_per_side
        scale = numerator / children_per_side
        return parent_x + (scale * offset)


class TreePlot:
    """A class for plotting decision trees."""

    def __init__(self):
        """Initializes the plotter."""
        self.window = tk.Tk()
        self.window.title("Plot")
        self.window.geometry("1800x900")
        self.canvas = tk.Canvas(self.window, width=1800, height=900, bg="white")
        self.texts = []
        self.canvas.pack()

    def __add_rectangle(self, x1, y1, x2, y2):
        """Adds a rectangle to the canvas."""
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", width=0)

    def __add_text(self, x, y, content):
        """Adds text to the canvas."""
        self.texts.append(self.canvas.create_text(x, y,
                                                  text=content,
                                                  fill="black", font=("Helvetica", 12)))

    def add_reason_text(self, position_x, x, position_y, y, child):
        """Adds the reason text to the canvas."""
        x_begin = (position_x + x) / 2
        y_begin = (position_y + y) / 2
        self.__add_rectangle(x_begin - 30, y_begin - 10, x_begin + 50, y_begin + 10)
        self.__add_text(x_begin, y_begin, f"{child.reason[child.reason.index(':') + 1:].strip()}")

    def texts_to_front(self, texts):
        """Brings the texts to the front."""
        for t in texts:
            self.canvas.tag_raise(t)

    def __root_jobs(self, x, goal):
        """Does the jobs only the root item should do once."""
        self.canvas.create_text(x, 20, text=f"Goal: {goal}", fill="black", font=("Helvetica", 18))
        self.texts_to_front(self.texts)
        self.window.mainloop()

    def __plot_node(self, x, y, tree):
        """Plots the node."""
        self.canvas.create_rectangle(x - 50, y - 10, x + 50, y + 10, fill="white", width=0)
        self.__add_text(x, y, f"{tree.data}")

    def plot(self, tree: Node, x=900, y=50, level=0, goal=""):
        """Plots the tree."""
        for i in range(len(tree.children)):
            position_x = calculate_new_x(i, len(tree.children), x, level)
            position_y = y + int((200 / (level + 1)))
            self.canvas.create_line(x, y, position_x, position_y, fill="blue", width=2)
            self.add_reason_text(position_x, x, position_y, y, tree.children[i])
            self.plot(tree.children[i], position_x, position_y, level + 1)

        self.__plot_node(x, y, tree)
        if level == 0:
            self.__root_jobs(x, goal)
