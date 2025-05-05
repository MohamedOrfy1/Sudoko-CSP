#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the script directory
cd "$SCRIPT_DIR"

# Function to cleanup on script exit
cleanup() {
    echo "Stopping servers..."
    # Kill the Python process (backend)
    pkill -f "uvicorn app.main:app"
    # Kill the Node process (frontend)
    pkill -f "vite"
    exit
}

# Trap SIGINT (Ctrl+C) and call cleanup
trap cleanup SIGINT

# Check if backend directory exists
if [ ! -d "backend" ]; then
    echo "Error: backend directory not found!"
    exit 1
fi

# Check if frontend directory exists
if [ ! -d "frontend/sudoku-solver" ]; then
    echo "Error: frontend/sudoku-solver directory not found!"
    exit 1
fi

echo "Starting backend server..."
cd backend
if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt not found in backend directory!"
    exit 1
fi
python -m uvicorn app.main:app --reload &
BACKEND_PID=$!

echo "Starting frontend server..."
cd ../frontend/sudoku-solver
if [ ! -f "package.json" ]; then
    echo "Error: package.json not found in frontend/sudoku-solver directory!"
    exit 1
fi
npm run dev &
FRONTEND_PID=$!

echo "Servers are running! Press Ctrl+C to stop."
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID 