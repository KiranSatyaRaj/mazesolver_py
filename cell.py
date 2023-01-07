from graphics import *

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = window

    def draw(self, p1, p2):
        if self.has_left_wall:
            self.__win.draw_line(
                line=Line(Point(p1.x, p1.y), Point(p1.x, p2.y)), fill_color='black'
            )
        if self.has_top_wall:
            self.__win.draw_line(
                line=Line(Point(p1.x, p1.y), Point(p2.x, p1.y)), fill_color='black'
            )
        if self.has_right_wall:
            self.__win.draw_line(
                line=Line(Point(p2.x, p1.y), Point(p2.x, p2.y)), fill_color='black'
            )
        if self.has_bottom_wall:
            self.__win.draw_line(
                line=Line(Point(p1.x, p2.y), Point(p2.x, p2.y)), fill_color='black'
                )