from graphics import *


class Cell:
    def __init__(self, win=None):
        self._has_left_wall = True
        self._has_right_wall = True
        self._has_top_wall = True
        self._has_bottom_wall = True
        self.__win = win

    def _x1(self):
        return self.__x1

    def _y1(self):
        return self.__y1

    def _x2(self):
        return self.__x2

    def _y2(self):
        return self.__y2

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.__win is None:
            return

        if self._has_left_wall:
            self.__win._draw_line(
                line=Line(Point(x1, y1), Point(x1, y2)), fill_color='black'
            )

        if self._has_top_wall:
            self.__win._draw_line(
                line=Line(Point(x1, y1), Point(x2, y1)), fill_color='black'
            )
        else:
            self.__win._draw_line(
                line=Line(Point(x1, y1), Point(x2, y1)), fill_color='white'
            )

        if self._has_right_wall:
            self.__win._draw_line(
                line=Line(Point(x2, y1), Point(x2, y2)), fill_color='black'
            )

        if self._has_bottom_wall:
            self.__win._draw_line(
                line=Line(Point(x1, y2), Point(x2, y2)), fill_color='black'
            )
        else:
            self.__win._draw_line(
                line=Line(Point(x1, y2), Point(x2, y2)), fill_color='white'
            )

    def draw_move(self, to_cell, undo=False):
        x1 = (self._x1() + self._x2()) // 2
        x2 = (to_cell._x1() + to_cell._x2()) // 2
        y1 = (self._y1() + self._y2()) // 2
        y2 = (to_cell._y1() + to_cell._y2()) // 2
        center_cell_1 = Point(x1, y1)
        center_cell_2 = Point(x2, y2)
        color = "red"
        if undo:
            color = "gray"

        self.__win._draw_line(
            line=Line(center_cell_1, center_cell_2), fill_color=color)
