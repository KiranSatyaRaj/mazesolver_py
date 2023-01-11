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
        win=None,
    ):
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

    def create_cells(self):
        self.cells = []
        for i in range(0, self.__num_rows):
            self.cells_row = []
            for j in range(0, self.__num_cols):
                self.__draw_cell(i, j)
                self.cells_row.append(j)
            self.cells.append(self.cells_row)
                
    def __draw_cell(self, i, j):
        point1 = Point(self.__cell_size_x * (j + 1), (i + 1) * self.__cell_size_y)
        point2 = Point(self.__cell_size_x * (j + 2), (i + 2) * self.__cell_size_y)

        c = Cell(win=self.__win, p1=point1, p2=point2)
        c.draw()
        self.__animate()
                
    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)


