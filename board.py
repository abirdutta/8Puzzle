#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Sahana Sreeprakash
# email: sahanas@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = int(digitstr[3*r + c])
                
                if self.tiles[r][c] == 0:
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ Returns a string representation for a Board object."""
        
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == 0:
                    s += "_ "
                else:
                    s += str(self.tiles[r][c]) + " "
                
            s += '\n'                
        return s
    
    def move_blank(self, direction):
        """takes input to modify board accordingly and move the tiles in it """
        new_row = 0
        new_col = 0

        if direction == 'up':
            new_row = self.blank_r - 1
            new_col = self.blank_c
            
            if new_row < 0 or new_row > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col]
                self.tiles[new_row][new_col] = 0
                self.blank_c = new_col
                self.blank_r = new_row
                return True
            
        elif direction == 'down':
            new_row = self.blank_r + 1
            new_col = self.blank_c
            if new_row < 0 or new_row > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col] 
                self.tiles[new_row][new_col] = 0
                self.blank_c = new_col
                self.blank_r = new_row
                return True
        elif direction == 'left':
            new_row = self.blank_r
            new_col = self.blank_c - 1
            if new_col < 0 or new_col > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col] 
                self.tiles[new_row][new_col] = 0
                self.blank_c = new_col
                self.blank_r = new_row
                return True
        elif direction == 'right':
            new_row = self.blank_r
            new_col = self.blank_c + 1
            if new_col < 0 or new_col > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col]  
                self.tiles[new_row][new_col] = 0
                self.blank_c = new_col
                self.blank_r = new_row
                return True
        else:
            print("Error: invalid direction")
            return False
        
            
        
    
    def digit_string(self):
        """creates and returns a string of digits that correspons to the current contents of the Board object's tiles attribute"""
        s = ''
        for r in range(3):
            for c in range(3):
                s += str(self.tiles[r][c])
        return s

    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of the called object"""
        new_board = Board(self.digit_string())
        return new_board
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object that are not where they should be in the goal state"""
        count = 0
        current = self.digit_string()
        goal = '012345678'

        for tile_ind in range(8):
            if current[tile_ind] != 0 and current[tile_ind] != goal[tile_ind] and goal[tile_ind] != 0:
                count += 1
        return count

    def __eq__(self, other):
        """overloads the == operator – creating a version of the operator that works for Board objects"""
        if self.digit_string() == other.digit_string():
            return True
        else:
            return False
                
                

        



if __name__ == "__main__":


    b = Board('142358607')
    print(b.tiles)
    print(b)
    print(b.move_blank('up'))
    print(b)
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)

    print(b.move_blank('down'))
    print(b)
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)

    print(b.move_blank('left'))
    print(b)
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)

    print(b.move_blank('right'))
    print(b)
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)

    print(b.move_blank('down'))
    print(b)
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)

    b1 = Board('142358067')
    print(b1.digit_string())
    print(b1)

    b2 = Board('142358607')
    print(b2)
    print(b2.num_misplaced())

    print(b2.move_blank('left'))
    print(b2.digit_string())

    print(b1==b2)

