import random
import copy
from app.core.solver import solve_board
from app.core.sudoku import Sudoku

def is_valid(r, c, val , board):
    for i in range(9):
        # Check row and column repeation
        if board[r][i] == val or board[i][c] == val:
            return False
        
    # Check block repetition
    block_row = 3 * (r // 3)
    block_col = 3 * (c // 3)

    for i in range(block_row, block_row + 3):
        for j in range(block_col, block_col + 3):
            if board[i][j] == val:
                return False
    return True

def fill(board):
    #  Recursively fill 
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                # nums = list('123456789')
                nums = list(range(1, 10))
                random.shuffle(nums)
                for val in nums:
                    if is_valid(r, c, val, board):
                        board[r][c] = val
                        if fill(board):
                            return True
                        board[r][c] = 0
                return False
    return True

def generate_full_board():
    # Use backtracking to fill the board 
    # Make sure it's valid
    board = [[0 for _ in range(9)] for _ in range(9)]

    fill(board)
    return board
    


def create_puzzle(board, difficulty="easy"):
    # Removes numbers from solved board to create puzzle
    levels = {
        "easy": 45,
        "medium": 50,
        "hard": 55,
        "extreme": 60
    }
    num_to_remove = levels.get(difficulty, 35)

    removed = 0

    while removed < num_to_remove:

        # Pick random cell to remove 
        r = random.randint(0, 8)
        c = random.randint(0, 8)

         
        if board[r][c] != 0: 
            # Not empty

            temp = board[r][c]
            board[r][c] = 0

            # temp_board = [''.join(str(num) if num != 0 else '0' for num in row) for row in board]
            # temp_board = board.copy()
            temp_board = copy.deepcopy(board)
            # print(f"temp_board: {temp_board}")

            solution = solve_board(Sudoku(board=temp_board))
            
            # Check if board is still solvable
            if solution:
                removed += 1
            else:
                # Not Unique Solution --> revert
                board[r][c] = temp

    print(f"Removed {removed} cells from the board.")
    # print(board)
    return board

def generate_puzzle(difficulty="easy"):

    # Fill few random cells using backtracking algorithm
    # Ensure that the puzzle is solvable
    full = generate_full_board()
    
    puzzle = create_puzzle(full, difficulty)
    return puzzle



if __name__ == "__main__":
    # Example usage
    difficulty = "hard"  # Change to "easy", "medium", or "hard" or "extreme"
    puzzle = generate_puzzle(difficulty)
    print("Generated Puzzle:")
    sudoku = Sudoku(board=puzzle)
    sudoku.print_board()
    print("Solving the puzzle...")
    if solve_board(sudoku):
        print("Solved Puzzle:")
        sudoku.print_board()
    else:
        print("No solution found.")
    