from graphics import *

def main():

    win = Window(800, 600)
    point1 = Point(10, 10)
    point2 = Point(100, 100)
    # win.draw_line(line1, 'black')
    cell = Cell()
    cell.draw(point1, point2, win)
    win.wait_for_close()


main()