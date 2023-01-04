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
        return self.matrix[position[0]][position[1]] != 'X'
            
    def check_valid_start(self, start):
        # first, we need to make sure that the start position is valid
        # we can do this by checking if the start position is within the matrix
        # we can also check if the start position is not X
        if not self.check_valid_square(start):
            return False
        # this means it is within bounds
        # now we need to check if it is not S
        return self.matrix[start[0]][start[1]] != 'S'
    
    def check_valid_end(self, end):
        # first, we need to make sure that the end position is valid
        # we can do this by checking if the end position is within the matrix
        # we can also check if the end position is not X
        if not self.check_valid_square(end):
            return False
        # this means it is within bounds
        # now we need to check if it is S
        return self.matrix[end[0]][end[1]] == 'S'
    
    def check_valid_jump(self, start, end):
        # the first case in which a jump is valid is if the start and end positions differ by 1 in either x or y
        # first, we look at an x axis jump
        sub_cond_one = abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 0
        # now we look at a y axis jump
        sub_cond_two = abs(start[0] - end[0]) == 0 and abs(start[1] - end[1]) == 1
        # now, we check if either condition is true
        if sub_cond_one or sub_cond_two:
            return True
        # now, we need to test a more complicated jump, where you are jumping over a frog
        # first we need to make sure that this is such a case
        # we can do this by checking if the start and end positions differ by 2 in either x or y
        # first, we look at an x axis jump
        sub_cond_one = abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 0
        # now we look at a y axis jump
        sub_cond_two = abs(start[0] - end[0]) == 0 and abs(start[1] - end[1]) == 2
        # in these cases, we need to make sure that it is jumping over a frog of the opposite color
        if sub_cond_one or sub_cond_two:
            # first, we need to find the frog that is being jumped over
            # we can do this by finding the midpoint between the start and end positions
            # we can do this by adding the start and end positions together and dividing by 2
            frog = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
            # now we need to check if the frog is of the opposite color
            # we can do this by checking if the frog is not the same color as the start frog
            return self.matrix[start[0]][start[1]] != self.matrix[frog[0]][frog[1]]
        # if none of the conditions are met, then the jump is invalid
        return False
    
    def check_valid_move(self, start, end):
        # first, we need to make sure that the start and end positions are valid
        # we can do this by checking if the start and end positions are within the matrix
        # we can also check if the start and end positions are not X
        if not self.check_valid_start(start) or not self.check_valid_end(end):
            return False
        # this means they are within bounds, and the start and end positions are valid.
        # now we need to make sure that the jump itself is valid
        return self.check_valid_jump(start, end)
    
    def move(self, start, end):
        # we just need to make sure that the move is valid first
        if not self.check_valid_move(start, end):
            return False
        # now we need to make the move
        # we need to move the content in the start position to the end position
        # and move the content in the end position to the start position
        # we can do this by swapping the content of the two positions
        self.matrix[start[0]][start[1]], self.matrix[end[0]][end[1]] = self.matrix[end[0]][end[1]], self.matrix[start[0]][start[1]]
        return True
    

    def simple_move_map_resolution(self, notation):
        mapping = {
            '1' : (0, 0),
            '2' : (0, 1),
            '3' : (1, 0),
            '4' : (1, 1),
            '5' : (1, 2),
            '6' : (2, 1),
            '7' : (2, 2)
        }
        if notation in mapping:
            return mapping[notation]
        return None
    

    def make_simple_move(self, start, end):
        start = self.simple_move_map_resolution(start)
        end = self.simple_move_map_resolution(end)
        if start == None or end == None:
            return False
        return self.move(start, end)




if __name__ == "__main__":
    x = FrogGame()
    x.print_matrix()