from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.new_Canvas = Canvas(self.__root, width=width, height=height, bg='white')
        self.new_Canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
        
    def draw_line(self, line, fill_color):
        line.draw(self.new_Canvas, fill_color)

    def close(self):
        self.__running = False

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
    
class Cell:
    def __init__(self, p1, p2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p1.y
        self.__win = window