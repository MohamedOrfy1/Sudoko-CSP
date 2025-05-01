from pydantic import BaseModel, Field, validator
from typing import List

class SudokuBoard(BaseModel):
    board: List[List[int]] = Field(..., description="9x9 Sudoku board with 0s for empty cells")
    
    @validator('board')
    def validate_board(cls, board):
        # Check if board is 9x9
        if len(board) != 9:
            raise ValueError("Board must be 9x9")
        
        for row in board:
            if len(row) != 9:
                raise ValueError("Each row must have 9 cells")
            
            # Check if all values are between 0-9
            for cell in row:
                if not (0 <= cell <= 9):
                    raise ValueError("Cell values must be between 0-9")
        
        return board

class SudokuSolution(BaseModel):
    solved: bool = Field(..., description="Whether the puzzle was solved successfully")
    board: List[List[int]] = Field(..., description="The solved 9x9 Sudoku board")