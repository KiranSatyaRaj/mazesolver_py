from graphics import *
from cell import *

def main():

    win = Window(800, 600)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(p1=Point(50, 50), p2=Point(100, 100))

    c = Cell(win)
    c.has_right_wall = False
    #c.draw(125, 125, 200, 200)
    c.draw(p1=Point(125, 125), p2=Point(200, 200))

    c = Cell(win)
    c.has_bottom_wall = False
    #c.draw(225, 225, 250, 250)
    c.draw(p1=Point(225, 225), p2=Point(250, 250))

    c = Cell(win)
    c.has_top_wall = False
    #c.draw(300, 300, 500, 500)
    c.draw(p1=Point(300, 300), p2=Point(500, 500))

    win.wait_for_close()


main()