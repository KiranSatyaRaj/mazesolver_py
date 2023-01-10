from graphics import *
from cell import *
from maze import *

def main():

    win = Window(800, 600)

    num_rows = 10
    num_cols = 10
    cell_size_x = 80
    cell_size_y = 60

    m = Maze(num_rows=num_rows, num_cols=num_cols, cell_size_x=cell_size_x, cell_size_y=cell_size_y, win=win)
    m.create_cells()


    win.wait_for_close()


main()