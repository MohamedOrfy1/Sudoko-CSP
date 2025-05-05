from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.solver import SudokuSolver

router = APIRouter()

class SudokuBoard(BaseModel):
    board: List[List[int]]

@router.post("/solve")
def solve_sudoku(board: SudokuBoard):
    """Solve a Sudoku puzzle and return detailed solving information"""
    solver = SudokuSolver()
    result = solver.solve(board.board)
    return result

@router.get("/generate")
def generate_sudoku(difficulty: str = "medium"):
    """Generate a new Sudoku puzzle"""
    # For now, return a simple puzzle
    puzzle = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    return {"board": puzzle} 