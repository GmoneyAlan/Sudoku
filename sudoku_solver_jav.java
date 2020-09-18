class Sudoku{
    //Implemented using backtracing
    public static boolean solve_sudoku(int[][] board){
        boolean board_solved = has_empty(board);
        int[] empty;
        if (!board_solved){
            return true;
        } else {
            empty = find_empty(board);
        }
        System.out.println(empty[0] + " " + empty[1]);
        for(int i = 1; i < 10; i++){
            board[empty[0]][empty[1]] = i;
            if(is_valid(empty,board)){
                if (solve_sudoku(board)){
                    return true;
                }
            }
            board[empty[0]][empty[1]] = 0;
        }
        return false;
    }

    private static int[] find_empty(int[][] board){
        int[] empty = new int[2];
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                if (board[i][j] == 0){
                    empty[0] = i;
                    empty[1] = j;
                    return empty;
                }
            }
        }
        return new int[2];
    }

    private static boolean has_empty(int[][] board){
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                if (board[i][j] == 0)
                    return true;
            }
        }
        return false;
    }

    private static boolean is_valid(int[] cell, int[][] board){
        //Check Row
        for(int i = 0; i < board[cell[0]].length; i++){
            if(cell[1] != i && board[i][cell[1]] == i)
                return false;
        }
        //Check Column
        for(int i = 0; i < board.length; i++){
            if(cell[0] != i && board[cell[0]][i] == i){
                return false;
            }
        }
        //Check cell block
        int A, B;
        if(cell[0] > 2){
            if(cell[0] > 5){
                A = 6;
            } else{
                A = 3;
            }
        } else{
            A = 0;
        }
        if(cell[1] > 2){
            if(cell[1] > 5){
                B = 6;
            } else{
                B = 3;
            }
        } else{
            B = 0;
        }

        for(int i = A; i < A+3; i++){
            for(int j = B; j < B+3; j++){
                if(board[i][j] == board[cell[0]][cell[1]] && ((cell[0] != i) || cell[1] != j)){
                    return false;
                }
            }
        }
        return true;
    }

    public static void print_board(int[][] board){
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board.length; j++){
                System.out.print(board[i][j] + " ");
                if(j == 2 || j == 5){
                    System.out.print("||");
                }
            }
            System.out.println();
            if(i == 2 || i == 5){
                for(int j = 0; j < 7; j++){
                        System.out.print("---");
                }
                System.out.println();
            }
        }    
            System.out.println();
    }
    
    public static void main(String[] args){
        int[][] board = {
             {5,3,0,0,7,0,0,0,0},
             {6,0,0,1,9,5,0,0,0},
             {0,9,8,0,0,0,0,6,0},
             {8,0,0,0,6,0,0,0,3},
             {4,0,0,8,0,3,0,0,1},
             {7,0,0,0,2,0,0,0,6},
             {0,6,0,0,0,0,2,8,0},
             {0,0,0,4,1,9,0,0,5},
             {0,0,0,0,8,0,0,7,9}
    };
  
    print_board(board);
    solve_sudoku(board);
    }
}