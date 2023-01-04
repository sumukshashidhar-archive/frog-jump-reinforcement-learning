class FrogGame:

    def __init__(self):
        # initialize the game with a matrix
        # we want it to look like this
        # W W X
        # W S B
        # X B B
        # where W is the white frog, S is the empty space, X is an untouchable square, and B is the black frog
        self.matrix = [
            ['W', 'W', 'X'],
            ['W', 'S', 'B'],
            ['X', 'B', 'B']
        ]
    
    def print_matrix(self):
        # to print the matrix, we want to print the frogs only, without the X and S
        # we can do this by looping through the matrix and printing each element
        for row in self.matrix:
            for element in row:
                if element != 'X' and element != 'S':
                    print(element, end=' ')
                else:
                    print(' ', end=' ')
            print()

    def check_valid_square(self, position):
        # first, we need to make sure that the position is valid
        # we can do this by checking if the position is within the matrix
        # we can also check if the position is not X
        if position[0] < 0 or position[0] > 2 or position[1] < 0 or position[1] > 2:
            return False
        # this means it is within bounds
        # now we need to check if it is not X
        if self.matrix[position[0]][position[1]] == 'X':
            return False
        # this means it is not X
        # now, we need to check if this is an empty square
        return self.matrix[position[0]][position[1]] == 'S'
            

    
    def check_valid_move(self, start, end):
        # first, we need to make sure that the start and end positions are valid
        # we can do this by checking if the start and end positions are within the matrix
        # we can also check if the start and end positions are not X
        if not self.check_valid_square(start) or not self.check_valid_square(end):
            return False
        # this means they are within bounds
        # now we need to check if the start and end positions are not the same
        if start == end:
            return False
        # this means they are not the same
        # now we need to check if the start and end positions are adjacent


if __name__ == "__main__":
    x = FrogGame()
    x.print_matrix()