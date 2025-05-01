from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sudoku Solver API",
    description="API for solving Sudoku puzzles using CSP with Arc Consistency",
    version="1.0.0"
)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Import and include API routes
from app.api.endpoints import router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Sudoku Solver API"}