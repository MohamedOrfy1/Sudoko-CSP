from fastapi import APIRouter, HTTPException
from app.models.schemas import SudokuBoard, SudokuSolution
from app.core.solver import solve_board
from app.core.sudoku import Sudoku

router = APIRouter(prefix="/api", tags=["sudoku"])

@router.post("/solve", response_model=SudokuSolution)
async def solve_sudoku(board: SudokuBoard):
    """
    Solve a Sudoku puzzle using CSP with Arc Consistency.
    
    The input board should be a 9x9 grid where:
    - 0 represents an empty cell
    - 1-9 represent filled cells
    """
    try:
        # Convert input board to Sudoku object
        sudoku = Sudoku(board.board)
         
        # Solve the board
        solved = solve_board(sudoku)
        
        if not solved:
            raise HTTPException(status_code=400, detail="The provided Sudoku puzzle is unsolvable")
        
        return {
            "solved": True,
            "board": sudoku.board
        }
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error solving Sudoku: {str(e)}")