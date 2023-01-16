from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self._new_Canvas = Canvas(
            self.__root, width=width, height=height, bg='white')
        self._new_Canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self._close)

    def _redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def _wait_for__close(self):
        self.__running = True
        while self.__running:
            self._redraw()
        print("window _closed...")

    def _draw_line(self, line, fill_color):
        line.draw(self._new_Canvas, fill_color)

    def _close(self):
        self.__running = False


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y


class Line:

    def __init__(self, _point1, _point2):
        self._point1 = _point1
        self._point2 = _point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self._point1._x, self._point1._y, self._point2._x, self._point2._y, fill=fill_color, width=2
        )

        canvas.pack(fill=BOTH, expand=1)
