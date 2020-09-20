'''
Sudoku
    81 cells in total
    fill in a 3 x 3 block with number from 1 - 9 NO REPEATS
    The number also cant repeat with a row and a columns
    
    We will use backtracing for this
'''

def solve_sudoku(board):
  #  print_board(board)
    is_solved = has_empty(board)
    if not is_solved:
        return True
    x, y = get_empty_cell(board)
    for i in range(1,10):
        board[x][y] = i
        if is_valid(x, y, board):
            if solve_sudoku(board):
                return True
        board[x][y] = 0        

def has_empty(board):
    for i in range(9):
        if 0 in board[i]:
            return True
    return False
    
def get_empty_cell(board):
    for i in range(9):
        for j in range(9):
            print(i, j, board[i][j])
            if board[i][j] == 0:
                return i, j

def is_valid(x, y, board):
    #Add condition for x
    #Checks if the row is valid
    for i in range(9):
        if board[x][i] == board[x][y] and i != y:
            #print(x, y,'i:',i,board[x][i],board[x][y])
            return False
    
    #Checks if the column is valid
    for i in range(9):
        if board[i][y] == board[x][y] and i != x:
            #print(x,y,'j:',i,board[i][y],board[x][y])
            return False
        
    '''
    The following code checks if the cell block (3x3), is valid by finding the cell block first
    '''
    if x > 2:
        if x > 5:
            A = 6
        else:
            A = 3
    else:
        A = 0
    if y > 2:
        if y > 5:
            B = 6
        else:
            B = 3
    else:
        B = 0
   # print('A:',A,'B:',B)
    for i in range(A, A+3):
        for j in range(B, B+3):
            if ((x != i) and (y != j)) and board[i][j] == board[x][y]:
                #print(x,y,'i:',i,'j:',j,board[x][y])
                return False   
    return True
    
def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j],end=' ')
            if j == 2 or j == 5:
                print('||',end='')
        print()
        if i == 2 or i == 5:
            for j in range(12):
                print('--',end='')
            print()
        
    
if __name__ == '__main__':
    board = [[5,3,0,0,7,0,0,0,0],
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,0],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9]
             ]
    
    solve_sudoku(board)
    
