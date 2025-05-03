import { useState } from 'react'
import './App.css'
import SudokuBoard from './components/SudokuBoard/SudokuBoard.jsx'
import Options from './components/Options/Options.jsx';

const emptyBoard = () => Array.from({ length: 9 }, () => Array(9).fill(0));

const exampleBoard = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 8, 0, 5],
  [0, 0, 0, 0, 7, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 7],
  [0, 0, 5, 0, 9, 0, 0, 8, 1],
  [0, 0, 7, 0, 0, 8, 5, 9, 3],
  [0, 0, 8, 0, 2, 3, 0, 7, 0],
  [0, 3, 9, 0, 0, 5, 0, 0, 0],
  [0, 7, 1, 0, 6, 0, 0, 0, 4]
]

function App() {
  const [board, setBoard] = useState(emptyBoard());

  function handleGenerate() {
    setBoard(samplePuzzle);
  };

  function handleClear() {
    setBoard(emptyBoard());
  };

  function handleInput() {
    const input = prompt('Enter the puzzle as a string (81 characters, 0 for empty cells):');
    if (input && input.length === 81) {
      const newBoard = [];
      for (let i = 0; i < 9; i++) {
        const row = input.slice(i * 9, (i + 1) * 9).split('').map(Number);
        newBoard.push(row);
      }
      setBoard(newBoard);
    } else {
      alert('Invalid input. Please enter a string of 81 characters.');
    }
  }

  function handleSolve() {
    alert('Need to connect to the solver');
  };

  return (
    <>
      <h1>Sudoku Solver</h1>
      <Options onClear={handleClear} onGenerate={handleGenerate} OnInput={handleInput} />
      <SudokuBoard board={board} setBoard={setBoard} />
      <button onClick={handleSolve}>Solve</button>
    </>
  )
}

export default App
