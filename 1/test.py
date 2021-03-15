import unittest

from tic_tac_toe import TicTacToe


class TestMoveMaking(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_basic_move(self):
        self.game._make_move(0, 0)

        self.assertEqual(self.game._board[0][0], 'x')

    def test_super_move(self):
        self.game._make_move(-1, -1)

        self.assertEqual(self.game._board[2][2], 'x')

    def test_duplicated_move(self):
        self.game._make_move(1, 1)

        self.assertRaises(TicTacToe.Error,
                          TicTacToe._make_move,
                          self.game, 1, 1)

    def test_value_error(self):
        self.assertRaises(TicTacToe.Error,
                          TicTacToe._make_move,
                          self.game, 'a', 'b')

    def test_index_error(self):
        self.assertRaises(TicTacToe.Error,
                          TicTacToe._make_move,
                          self.game, 5, 5)


class VictoryTest(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_diagonal_validation(self):
        self.game._make_move(0, 0)
        self.game._make_move(1, 1)
        self.game._make_move(2, 2)

        self.assertTrue(self.game._is_victory())

    def test_row_validation(self):
        self.game._make_move(0, 0)
        self.game._make_move(0, 1)
        self.game._make_move(0, 2)

        self.assertTrue(self.game._is_victory())

    def test_column_validation(self):
        self.game._make_move(0, 0)
        self.game._make_move(1, 0)
        self.game._make_move(2, 0)

        self.assertTrue(self.game._is_victory())


if __name__ == '__main__':
    unittest.main()
