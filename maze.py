from graphics import *
from cell import *
import time

class Maze:
    def __init__(
        self,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

    def create_cells(self):
        for i in range(0, self.__num_rows):
            for j in range(0, self.__num_cols):
                self.__draw_cell(i, j)
                
    def __draw_cell(self, i, j):
        point1 = Point(j * self.__cell_size_x, i * self.__cell_size_y)
        point2 = Point(self.__cell_size_x * (j + 1), (i + 1) * self.__cell_size_y)

        c = Cell(window=self.__win, p1=point1, p2=point2)
        c.draw()
        self.__animate()
                
    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
