import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(num_rows, num_cols, 10, 10)
        m1._create_cells()
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(num_rows, num_cols, 10, 10)
        m1._create_cells()
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0]._has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows-1][num_cols-1]._has_bottom_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()
