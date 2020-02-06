"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    l = 0 
    m = 0
    n = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                l +=1
            elif board[i][j] == "X":
                m += 1
            elif board[i][j] == "O":
                n += 1

    #print(l,m,n)
    if l == 9:
        return X
    if m > n:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                free = (i,j)
                action.add(free)
    
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (board[action[0]][action[1]]) != None:
        raise Exception("Invalid Action")
    
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)
        
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        # row check
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            #print("Row 1 X", i)
            return X
        # column check
        elif board[0][i] == X and board[1][i] == X and board[2][i] == X:
            #print("column X", i)
            return X
        # row check
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            #print("Row 1 O", i)
            return O
        # column check
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            #print("Column 1 O", i)
            return O
        
    # diagonal check X
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    # diagonal check O
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif actions(board) == set():
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_move = None
    """Max function"""
    def maxValue(board):
        nonlocal best_move
        if terminal(board):
                return utility(board)

        best = -math.inf

        for action in actions(board):

            score = minValue(result(board, action))
            
            if score > best:
                best = score
                best_move = action
                #print(best_move)
        return best

    """Min function"""
    def minValue(board):
        nonlocal best_move
        if terminal(board):
                return utility(board)

        best = math.inf

        for action in actions(board):
            
            score = maxValue(result(board, action))
            
            if score < best:
                best = score
                best_move = action
                #print(best_move)
        return best


    # check player who has the next turn on a board
    if player(board) == X:
        emptycells = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    emptycells += 1
        if emptycells == 9:
            return (1,1)
        else:
            move = maxValue(board)
    else:
        move = minValue(board)

    return best_move