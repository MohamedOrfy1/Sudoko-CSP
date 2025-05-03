import React from 'react';
import './Options.css';

const Options = ({ onGenerate, OnInput, onClear }) => {
  return (
    <div className="options">
      <button onClick={onGenerate}>Generate Puzzle</button>
      <button onClick={OnInput}>Input New Puzzle</button>
      <button onClick={onClear}>Clear Board</button>
    </div>
  );
};

export default Options;
