import { useState } from 'react'
import './App.css'
import SudokuBoard from './components/SudokuBoard/SudokuBoard.jsx'
import Options from './components/Options/Options.jsx';

const emptyBoard = () => Array.from({ length: 9 }, () => Array(9).fill(0));

function App() {
  const [board, setBoard] = useState(emptyBoard());
  const [editable, setEditable] = useState(
    Array.from({ length: 9 }, () => Array(9).fill(true))
  );
  
  const [error, setError] = useState(null);
  const [isSolving, setIsSolving] = useState(false);

  async function handleGenerate(difficulty) {
    try {
      setError(null);
      const response = await fetch(`http://localhost:8000/api/generate?difficulty=${difficulty}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      setBoard(data.board);
      setEditable(data.board.map(row => row.map(cell => cell === 0)));
    } catch (error) {
      setError('Failed to generate puzzle. Please try again.');
      console.error('Error generating puzzle:', error);
    }
  };

  function handleClear() {
    setBoard(emptyBoard());
    setEditable(Array.from({ length: 9 }, () => Array(9).fill(true)));
    setError(null);
  };

  function handleInput() {
    const input = prompt('Enter the puzzle as a string (81 characters, 0 for empty cells):');
    if (input && input.length === 81) {
      const newBoard = [];
      const newEditable = [];
      for (let i = 0; i < 9; i++) {
        const row = input.slice(i * 9, (i + 1) * 9).split('').map(Number);
        newBoard.push(row);
        newEditable.push(row.map(cell => cell === 0));
      }
      setBoard(newBoard);
      setEditable(newEditable);
      setError(null);
    } else {
      setError('Invalid input. Please enter a string of 81 characters.');
    }
  }

  async function handleSolve() {
    try {
      setError(null);
      setIsSolving(true);

      const response = await fetch('http://localhost:8000/api/solve', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          board: board
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      if (!data.solved) {
        setError('The puzzle could not be solved. Please check your input.');
        return;
      }

      setBoard(data.board);
      setEditable(Array.from({ length: 9 }, () => Array(9).fill(false)));
    } catch (error) {
      setError('Failed to solve puzzle. Please try again.');
      console.error('Error solving puzzle:', error);
    } finally {
      setIsSolving(false);
    }
  };

  return (
    <>
      <h1>Sudoku Solver</h1>
      <Options onClear={handleClear} onGenerate={handleGenerate} OnInput={handleInput} />
      {error && <div className="error">{error}</div>}
      <div className="sudoku-container">
        <SudokuBoard board={board} setBoard={setBoard} editable={editable} />
        <button 
          onClick={handleSolve} 
          disabled={isSolving}
          className={isSolving ? 'solving' : ''}
        >
          {isSolving ? 'Solving...' : 'Solve'}
        </button>
      </div>
    </>
  )
}

export default App
