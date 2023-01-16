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
        self._cells = []

    def _create_cells(self):
        for i in range(0, self.__num_rows):
            row_cells = []
            for j in range(0, self.__num_cols):
                row_cells.append(Cell(self.__win))
            self._cells.append(row_cells)

        for i in range(0, self.__num_rows):
            for j in range(0, self.__num_cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.__cell_size_x * (j + 1)
        y1 = (i + 1) * self.__cell_size_y
        x2 = self.__cell_size_x * (j + 2)
        y2 = (i + 2) * self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self._cells[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)
