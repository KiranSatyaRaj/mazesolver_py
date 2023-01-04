from graphics import *

def main():

    win = Window(800, 600)
    line1 = Line(Point(0, 0), Point(100, 100))
    line2 = Line(Point(100, 0), Point(200, 100))
    win.draw_line(line1, 'black')
    win.draw_line(line2, 'red')
    win.wait_for_close()


main()