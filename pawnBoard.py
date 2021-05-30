# Author:Jesse Zelaya
# Date: May 20th, 2020
# Description: Pawn Board game allows user to user their own program to call on functions
#              for this game. It is a 4 x 4 board that uses chess pawn rules and the game is
#              won when either player reaches the other player's starting row.


class PawnBoard:
    def __init__(self):
        """
        Class users two private variables _board_list and _board_state to
        create a 4 x 4 board which allows a user to play a game of pawns
        """
        row_3 = ["o", "o", "o", "o"]
        row_2 = ["", "", "", ""]
        row_1 = ["", "", "", ""]
        row_0 = ["x", "x", "x", "x"]

        self._board_list = [row_0, row_1, row_2, row_3]
        self._board_state = "UNFINISHED"

    def _check_draw(self):
        """
        At the end of a move, this checks to see if the move caused a draw
        by looking at each player's pieces and their available moves, if any.
        :return: returns True if draw
        """
        draw_bool = True
        # check for draw in middle sections for "x" and "o" only for middle positions
        for j in range(0,len(self._board_list)):
            for k in range(0, len(self._board_list)):
                # check for side cases for x at column 0
                if k == 0 and self._board_list[j][k] == "x":
                    if (self._check_legal_moves(j, k, j + 1, k) is True) or \
                            (self._check_legal_moves(j, k, j + 1, k + 1)):
                        #print("column 0 x move available")
                        return False
                # check for column 3 for x moves available
                elif k == 3 and self._board_list[j][k] == "x":
                    if (self._check_legal_moves(j, k, j + 1, k) is True) or \
                            (self._check_legal_moves(j, k, j + 1, k - 1) is True):
                        #print("column at 3 for x move available")
                        return False
                # check for middle cases for x (columns 1 and 2)
                elif (k == 1 or k == 2) and self._board_list[j][k] == "x":
                    if (self._check_legal_moves(j, k, j + 1, k -1) is True) or \
                            (self._check_legal_moves(j, k, j +1, k) is True) or \
                            (self._check_legal_moves(j, k, j + 1, k + 1) is True):
                        #print("middle case true!")
                        return False
                # check for column 0 cases for "o"
                elif k == 0 and self._board_list[j][k] == "o":
                    if (self._check_legal_moves(j, k, j - 1, k + 1) is True) or \
                            (self._check_legal_moves(j, k, j - 1, k) is True):
                        #print("column 0 o move available")
                        return False
                # check for column 3 cases for "o"
                elif k == 3 and self._board_list[j][k] == "o":
                    if (self._check_legal_moves(j, k, j - 1, k) is True) or \
                            (self._check_legal_moves(j, k, j - 1, k - 1) is True):
                        #print("column 3 move available for o")
                        return False
                # check middle cases for o
                elif (k == 1 or k == 2) and self._board_list[j][k] == "o":
                    if (self._check_legal_moves(j, k, j - 1, k - 1) is True) or \
                            (self._check_legal_moves(j, k, j - 1, k) is True) or \
                            (self._check_legal_moves(j, k, j - 1, k + 1) is True):
                        #print("legal move in middle columns available for o")
                        return False
        # if no cases offer legal moves return True and game is a draw
        return draw_bool

    def _check_legal_moves(self, row_from, col_from, row_to, col_to):
        """
        Checks for legal moves and board_state for a given piece
        :param row_from: row coordinate, piece being moved
        :param col_from: column coordinate, piece being moved
        :param row_to: row coordinate of where to move piece
        :param col_to: row coordinate of where to move piece
        :return: false if there is a legal move, true if not
        """
        # check board state if there is an actual piece to move
        if self._board_state == "X_WON" or self._board_state == "O_WON" \
                or self._board_state == "DRAW" \
                or self._board_list[row_from][col_from] == "":
            #print("invalid board state or no pawn to move")
            return False
        # check if move is greater than 1 space
        elif (abs(row_to - row_from) > 1) or (abs(col_to - col_from) > 1):
            # print("move is greater than 1 space")
            return False
        # check if moving backwards
        elif (self._board_list[row_from][col_from] == "x" and row_from > row_to) or \
                (self._board_list[row_from][col_from] == "o" and row_from < row_to):
            #print("moving backwards")
            return False
        # check if moving right or left
        elif row_from == row_to:
            #print("cant move side to side")
            return False
        elif col_from == col_to and self._board_list[row_to][col_to] == "":
            #print("move ahead legal")
            return True
        # check for diagonal moves for edges (works for  x's)
        elif self._board_list[row_from][col_from] == "x":
            if col_from == 0 and col_from + 1 == col_to and \
                    self._board_list[row_to][col_to] == "o":
                #print("Legal diagonal move from 0,0 to 1,1")
                return True
            elif col_from == 3 and col_from - 1 == col_to and \
                    self._board_list[row_to][col_to] == "o":
                #print("hi")
                return True
            # checking middle cases for x
            elif (col_from + 1 == col_to or col_from - 1 == col_to) and \
                    self._board_list[row_to][col_to] == "o":
                #print("valid middle diagonal move for x")
                return True
            # check edge cases for o
        elif self._board_list[row_from][col_from] == "o":
            if col_from == 0 and col_from + 1 == col_to and \
                    self._board_list[row_to][col_to] == "x":
                #print("legal move from 3,0 to 2,1")
                return True
            elif (col_from == 3 and col_from - 1 == col_to) and \
                    (self._board_list[row_to][col_to]) == "x":
                #print("legal move from 3,3 to 2,2")
                return True

            elif (col_from + 1 == col_to or col_from - 1 == col_to) and \
                    self._board_list[row_to][col_to] == "x":
                #print("valid middle diagonal move for o")
                return True
        else:
            return False

    def make_move(self, row_from, col_from, row_to, col_to):
        """
        Makes pawn move, given coordinates from user
        checks legal moves, updates current state
        :param row_from: players piece to move at row
        :param col_from: players piece to move at col
        :param row_to: where to attempt player move row
        :param col_to: where to attempt player move col
        :return: False if draw, or no legal moves
        """
        # check legal moves, if true it will continue
        if self._check_legal_moves(row_from, col_from, row_to, col_to) is True:
            # make move and update current_state
            self._board_list[row_to][col_to] = self._board_list[row_from][col_from]
            self._board_list[row_from][col_from] = ""
            if self._board_list[row_to][col_to] == "x" and row_to == 3:
                self._board_state = "X_WON"
                return True
            elif self._board_list[row_to][col_to] == "o" and row_to == 0:
                self._board_state = "O_WON"
                return True
            if self._check_draw() is True:
                # print("game is draw")
                self._board_state = "DRAW"
                return True
            else:
                self._board_state = "UNFINISHED"
                return True
        else:
            return False

    def get_current_state(self):
        """
        returns user the current state of the board
        :return: _current_state
        """
        return self._board_state

    def printer(self):
        """
        prints board with current placement
        :return: nothing
        """
        print("\n")
        for nn in range(len(self._board_list) - 1, -1, -1):
            print(self._board_list[nn])


# game test lines
n = PawnBoard()
# n.printer()
n.make_move(0, 3, 1, 3)
n.printer()
print(n.get_current_state())

n.printer()
print(n.get_current_state())
n.make_move(3, 3, 2, 3)
n.printer()
print(n.get_current_state())

n.make_move(0, 3, 1, 3)
n.printer()

print(n.get_current_state())


