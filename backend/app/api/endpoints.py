from fastapi import APIRouter, HTTPException
from app.models.schemas import SudokuBoard, SudokuSolution
from app.core.solver import solve_board
from app.core.sudoku import Sudoku
from app.core.generator import generate_puzzle

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

@router.get("/generate", response_model=SudokuBoard)
async def generate_sudoku(difficulty: str = "easy"):
    """
    Generate a new Sudoku puzzle.
    
    Args:
        difficulty (str): The difficulty level of the puzzle. Can be "easy", "medium", "hard", or "extreme".
                         Defaults to "easy".
    
    Returns a 9x9 grid where:
    - 0 represents an empty cell
    - 1-9 represent filled cells
    """
    try:
        # Generate a new puzzle with specified difficulty
        puzzle, full = generate_puzzle(difficulty)
        
        return {
            "board": puzzle,
            "full_board": full
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating Sudoku: {str(e)}")