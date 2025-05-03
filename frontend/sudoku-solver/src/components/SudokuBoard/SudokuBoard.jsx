import React from 'react';
import './SudokuBoard.css';

const SudokuBoard = ({ board, setBoard }) => {

    const handleChange = (row, col, value) => {
        const newValue = value === '' ? 0 : parseInt(value, 10);
        if (isNaN(newValue) || newValue < 0 || newValue > 9) {
            return;
        }
        const newBoard = board.map((row) => [...row]);
        newBoard[row][col] = newValue;
        setBoard(newBoard);
    };

    return (
        <>
            <div className="sudoku-board">
                {board.map((row, rowIndex) => (
                    <div className="sudoku-row" key={rowIndex}>
                        {row.map((cell, colIndex) => (
                            <input
                                key={`${rowIndex}-${colIndex}`}
                                className="sudoku-cell"
                                type="text"
                                value={cell === 0 ? '' : cell}
                                onChange={(e) => handleChange(rowIndex, colIndex, e.target.value)}
                                maxLength={1}
                            />
                        ))}
                    </div>
                ))}
            </div>
        </>
    );
};

export default SudokuBoard;
