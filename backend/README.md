
## 1. Install requirements :
```pip install -r requirements.txt```

## 2- Running the Server:
```uvicorn app.main:app --reload```

### File Structure:
```
app/
│
├── main.py
│   - Entry point for FastAPI app.
│
├── api/
│   └── endpoints.py
│       - Defines the `/solve` endpoint for solving Sudoku.
│
├── core/
│   ├── solver.py
│   │   - Contains the backtracking algo.
│   ├── generator.py
│   │   - Generates solvable Sudoku puzzles.
│   └── utils.py
│       - Shared utility functions
│
├── models/
│   └── schemas.py
│       - Pydantic models for validating incoming request data.

```

