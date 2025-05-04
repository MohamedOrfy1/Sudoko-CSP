import React, { useState } from 'react';
import './Options.css';

const Options = ({ onGenerate, OnInput, onClear }) => {
  const [difficulty, setDifficulty] = useState('easy');

  return (
    <div className="options">
      <div className="difficulty-selector">
        <label htmlFor="difficulty">Difficulty: </label>
        <select 
          id="difficulty" 
          value={difficulty} 
          onChange={(e) => setDifficulty(e.target.value)}
        >
          <option value="easy">Easy</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
          <option value="extreme">Extreme</option>
        </select>
      </div>
      <button onClick={() => onGenerate(difficulty)}>Generate Puzzle</button>
      <button onClick={OnInput}>Input New Puzzle</button>
      <button onClick={onClear}>Clear Board</button>
    </div>
  );
};

export default Options;
