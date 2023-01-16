from graphics import *
from cell import *
from maze import *

def main():

    win = Window(1000, 800)

    num_rows = 14
    num_cols = 18
    cell_size_x = 50
    cell_size_y = 50

    m = Maze(num_rows=num_rows, num_cols=num_cols, cell_size_x=cell_size_x, cell_size_y=cell_size_y, win=win)
    m._create_cells()
    m._break_entrance_and_exit()


    win.wait_for_close()


main()