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
        self.__point1 = Point(self.__cell_size_x * (j + 1), (i + 1) * self.__cell_size_y)
        self.__point2 = Point(self.__cell_size_x * (j + 2), (i + 2) * self.__cell_size_y)

        self.__c = Cell(win=self.__win, p1=self.__point1, p2=self.__point2)
        if  i == 0 and j == 0:
            self.__c.has_top_wall = False
            self.__c.has_bottom_wall = False
            self.__c.has_right_wall = False
        if  i == self.__num_rows - 1 and j == self.__num_cols - 1:
            self.__c.has_top_wall = False
            self.__c.has_bottom_wall = False
            self.__c.has_left_wall = False
        self.__c.draw()
        self.__animate()
                
    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    # def break_entrance_and_exit(self):
    #     self.__point1 = Point(self.__cell_size_x, self.__cell_size_y) 
    #     self.__point2 = Point(self.__cell_size_x * 2, self.__cell_size_y * 2)
    #     self.__c.has_top_wall = False
    #     self.__c.has_bottom_wall = False
    #     self.__c.has_right_wall = False
    #     self.__draw_cell(0, 0)
    #     if self.__point1 == Point(
    #         self.__cell_size_x * self.__num_cols , self.__cell_size_y * self.__num_rows
    #         ) and self.__point2 == Point(
    #             self.__cell_size_x * (self.__num_cols + 1), self.__cell_size_y * (self.__num_rows + 1)
    #             ):
    #         self.__c.has_top_wall = False
    #         self.__c.has_bottom_wall = False
    #         self.__c.has_left_wall = False
    #         self.__draw_cell(self.__num_rows, self.__num_cols)         


