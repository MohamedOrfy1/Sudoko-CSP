import React from 'react';
import './SudokuBoard.css';

const SudokuBoard = ({ board, setBoard, editable, setEditable, solution }) => {

    const handleChange = (row, col, value) => {
        const newValue = value === '' ? 0 : parseInt(value, 10);
        if (isNaN(newValue) || newValue < 0 || newValue > 9) {
            return;
        }
        const newBoard = [...board];
        newBoard[row][col] = newValue;
        setBoard(newBoard);
        if (solution === null) {
            const newEditable = [...editable];
            newEditable[row][col] = newValue === 0;
            setEditable(newEditable);
        }
    };

    const getCellClass = (row, col) => {
        if (!editable[row][col]) return 'fixed';
        if (editable[row][col] && solution === null) return 'fixed';
        const userValue = board[row][col];
        const correctValue = solution?.[row]?.[col];

        if (userValue === 0) return 'editable';
        if (userValue === correctValue) return 'correct';
        return 'incorrect';
    };

    return (
        <>
            <div className="sudoku-board">
                {board.map((row, rowIndex) => (
                    <div className="sudoku-row" key={rowIndex}>
                        {row.map((cell, colIndex) => (
                            <input
                                key={`${rowIndex}-${colIndex}`}
                                className={`sudoku-cell ${getCellClass(rowIndex, colIndex)}`}
                                type="text"
                                value={cell === 0 ? '' : cell}
                                onChange={(e) => 
                                    (editable[rowIndex][colIndex] &&
                                    handleChange(rowIndex, colIndex, e.target.value))}
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
