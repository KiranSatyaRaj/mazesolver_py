from graphics import *

class Cell:
    def __init__(self, window, p1, p2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.__win = window
    
    def x1(self):
        return self.__x1

    def y1(self):
        return self.__y1

    def x2(self):
        return self.__x2

    def y2(self):
        return self.__y2


    def draw(self):
        p1 = Point(self.x1(), self.y1())
        p2 = Point(self.x2(), self.y2())
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

    def draw_move(self, to_cell, undo=False):
        x1 = (self.x1() + self.x2()) // 2
        x2 = (to_cell.x1() + to_cell.x2()) // 2
        y1 = (self.y1() + self.y2()) // 2
        y2 = (to_cell.y1() + to_cell.y2()) // 2
        center_cell_1 = Point(x1, y1)
        center_cell_2 = Point(x2, y2)
        color = "red"
        if undo:
            color = "gray"
        
        self.__win.draw_line(line=Line(center_cell_1, center_cell_2), fill_color=color)