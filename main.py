from graphics import *
from cell import *
from maze import *

def main():

    win = Window(800, 600)

    num_rows = 20
    num_cols = 20
    cell_size_x = 40
    cell_size_y = 30

    m = Maze(num_rows=num_rows, num_cols=num_cols, cell_size_x=cell_size_x, cell_size_y=cell_size_y, win=win)
    m.create_cells()


    win.wait_for_close()


main()