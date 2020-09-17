'''
Sudoku
    81 cells in total
    fill in a 3 x 3 block with number from 1 - 9 NO REPEATS
    The number also cant repeat with a row and a columns

    build board
    Check if the board has empty cells
    if it does try to solve using the algorithm where there are no repeats in a row/column and block
    
    road map
    check if board has empty cells
    get cell solve it
    check if valid
    repeat
'''

def solve_sudoku(board):
    print('Board that needs to be solved')
    print_board(board)
    if if_has_empty(board):
        x, y = get_empty_cell(board)
        solve_cell(x,y,board)
        
def solve_cell(x,y,board):
    return 0

def if_has_empty(board):
    for i in range(10):
        for j in range(10):
            if board[i][j] == ' ':
                return True
    return False
    
def get_empty_cell(board):
    for i in range(10):
        for j in range(10):
            if board[i][j] == ' ':
                return i, j
        
def is_valid(x, y, board):
    for i in range(10):
        if board[x][i] == board[x][y]:
            return False
    
    for i in range(10):
        if board[i][y] == board[x][y]:
            return False
        
    for i in range()
    return True
    
def print_board(board):
    for i in range(10):
        for j in range(10):
            print(board[i][j],end=' ')
            if j is 3:
                print('||',end='')
            if i is 3:
                print('--',end='')
        
    
if __name__ == '__main__':
    board = [[],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             []
             ]
    solve_sudoku(board)
    