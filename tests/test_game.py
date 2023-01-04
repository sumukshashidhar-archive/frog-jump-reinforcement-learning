import unittest
from src.game import FrogGame
class TestFrogGame(unittest.TestCase):

    # Test that the game is initialized correctly
    def test_init(self):
        game = FrogGame()
        self.assertEqual(game.matrix, [
            ['W', 'W', 'X'],
            ['W', 'S', 'B'],
            ['X', 'B', 'B']
        ])
    
    # # Test that the matrix is printed correctly
    # def test_print_matrix(self):
    #     game = FrogGame()
    #     self.assertEqual(game.print_matrix(), None)
    
    # Test that the check_valid_square function works correctly
    def test_check_valid_square(self):
        game = FrogGame()
        self.assertEqual(game.check_valid_square((0, 0)), True)
        self.assertEqual(game.check_valid_square((0, 1)), True)
        self.assertEqual(game.check_valid_square((0, 2)), False)
        self.assertEqual(game.check_valid_square((1, 0)), True)
        self.assertEqual(game.check_valid_square((1, 1)), True)
        self.assertEqual(game.check_valid_square((1, 2)), True)
        self.assertEqual(game.check_valid_square((2, 0)), False)
        self.assertEqual(game.check_valid_square((2, 1)), True)
        self.assertEqual(game.check_valid_square((2, 2)), True)
        self.assertEqual(game.check_valid_square((-1, 0)), False)
        self.assertEqual(game.check_valid_square((0, -1)), False)
        self.assertEqual(game.check_valid_square((3, 0)), False)
        self.assertEqual(game.check_valid_square((0, 3)), False)
    
    # Test that the check_valid_start function works correctly
    def test_check_valid_start(self):
        game = FrogGame()
        self.assertEqual(game.check_valid_start((0, 0)), True)
        self.assertEqual(game.check_valid_start((0, 1)), True)
        self.assertEqual(game.check_valid_start((0, 2)), False)
        self.assertEqual(game.check_valid_start((1, 0)), True)
        self.assertEqual(game.check_valid_start((1, 1)), False)
        self.assertEqual(game.check_valid_start((1, 2)), True)
        self.assertEqual(game.check_valid_start((2, 0)), False)
        self.assertEqual(game.check_valid_start((2, 1)), True)
        self.assertEqual(game.check_valid_start((2, 2)), True)
        self.assertEqual(game.check_valid_start((-1, 0)), False)
        self.assertEqual(game.check_valid_start((0, -1)), False)
        self.assertEqual(game.check_valid_start((3, 0)), False)
        self.assertEqual(game.check_valid_start((0, 3)), False)
    
    # Test that the check_valid_end function works correctly
    def test_check_valid_end(self):
        game = FrogGame()
        self.assertEqual(game.check_valid_end((0, 0)), False)
        self.assertEqual(game.check_valid_end((0, 1)), False)
        self.assertEqual(game.check_valid_end((0, 2)), False)
        self.assertEqual(game.check_valid_end((1, 0)), False)
        self.assertEqual(game.check_valid_end((1, 1)), True)
        self.assertEqual(game.check_valid_end((1, 2)), False)
        self.assertEqual(game.check_valid_end((2, 0)), False)
        self.assertEqual(game.check_valid_end((2, 1)), False)
        self.assertEqual(game.check_valid_end((2, 2)), False)
        self.assertEqual(game.check_valid_end((-1, 0)), False)
        self.assertEqual(game.check_valid_end((0, -1)), False)
        self.assertEqual(game.check_valid_end((3, 0)), False)
        self.assertEqual(game.check_valid_end((0, 3)), False)
    
    # Test that the check_valid_move function works correctly
    def test_check_valid_move(self):
        game = FrogGame()
        self.assertEqual(game.check_valid_move((0, 0), (0, 1)), False)
        self.assertEqual(game.check_valid_move((0, 0), (1, 0)), False)
        self.assertEqual(game.check_valid_move((0, 0), (1, 1)), False)
        self.assertEqual(game.check_valid_move((0, 0), (0, 2)), False)
        self.assertEqual(game.check_valid_move((0, 0), (2, 0)), False)
        self.assertEqual(game.check_valid_move((0, 0), (2, 2)), False)
        self.assertEqual(game.check_valid_move((0, 0), (1, 2)), False)
        self.assertEqual(game.check_valid_move((0, 0), (2, 1)), False)
        self.assertEqual(game.check_valid_move((0, 0), (0, 0)), False)
        self.assertEqual(game.check_valid_move((0, 0), (0, -1)), False)
        self.assertEqual(game.check_valid_move((0, 0), (-1, 0)), False)
        self.assertEqual(game.check_valid_move((0, 0), (3, 0)), False)
        self.assertEqual(game.check_valid_move((0, 0), (0, 3)), False)
        self.assertEqual(game.check_valid_move((0, 0), (3, 3)), False)
        self.assertEqual(game.check_valid_move((0, 1), (0, 0)), False)
        self.assertEqual(game.check_valid_move((0, 1), (1, 0)), False)
        self.assertEqual(game.check_valid_move((0, 1), (1, 1)), True)
        self.assertEqual(game.check_valid_move((0, 1), (0, 2)), False)
        self.assertEqual(game.check_valid_move((0, 1), (2, 0)), False)
        self.assertEqual(game.check_valid_move((0, 1), (2, 2)), False)
        self.assertEqual(game.check_valid_move((0, 1), (1, 2)), False)
        self.assertEqual(game.check_valid_move((0, 1), (2, 1)), False)
        self.assertEqual(game.check_valid_move((0, 1), (0, 1)), False)
        self.assertEqual(game.check_valid_move((0, 1), (0, -1)), False)
        # now, let us test some other moves
        self.assertEqual(game.check_valid_move((1, 0), (1, 1)), True)
        self.assertEqual(game.check_valid_move((2, 1), (1, 1)), True)
        self.assertEqual(game.check_valid_move((1, 2), (1, 1)), True)
    

    # now let us test the move function
    def test_move(self):
        # initialize the game
        game = FrogGame()
        # test that the move function works correctly
        self.assertEqual(game.move((0, 1), (1, 1)), True)
        # now check that the frog has moved, by checking the board
        self.assertEqual(game.matrix, [
            ['W', 'S', 'X'],
            ['W', 'W', 'B'],
            ['X', 'B', 'B']
        ])
        # let us check the jumping over move
        self.assertEqual(game.move((2, 1), (0, 1)), True)
        self.assertEqual(game.matrix, [
            ['W', 'B', 'X'],
            ['W', 'W', 'B'],
            ['X', 'S', 'B']
        ])





