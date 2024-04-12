// WaterErosion.jsx
import React, { useState } from 'react';

const Card = ({ title, text, onClick, className }) => (
  <div className={`card ${className}`} onClick={onClick}>
    <h2>{title}</h2>
    <p>{text}</p>
  </div>
);

const WaterErosion = () => {
  // Component logic here
};

export default WaterErosion;
