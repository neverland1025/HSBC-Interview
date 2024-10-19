#### 1 Quiz.py

'''

Your `quiz.py` should have the following content.

 
'''

 

def reverse_list(l:list):

    """
    Reverse a list without using any built-in functions.

    Parameters:
        l (list): A list containing any type of data.

    Returns:
        _type_: list
    """   
    
    reversed_list = []
    
    for i in range(len(l) - 1, -1, -1):
        reversed_list.append(l[i])
    
    return reverse_list


#######quiz 2#######
def solve_sudoku(board):
    def is_valid(num, row, col):
        # Check if the num is not in the current row
        for x in range(9):
            if board[row][x] == num:
                return False
        
        # Check if the num is not in the current column
        for x in range(9):
            if board[x][col] == num:
                return False
        
        # Check if the num is not in the current 3x3 box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:  # Find an empty cell
                    for num in range(1, 10):  # Try all possible numbers
                        if is_valid(num, i, j):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0  # Backtrack
                    return False
        return True  # If no empty cell is left, the puzzle is solved
    
    solve()
    return board

