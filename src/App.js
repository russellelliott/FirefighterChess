import React, { useState } from 'react';
import { Chessboard } from 'react-chessboard';
import './App.css';

function App() {
  const starter = 'rnbqkbnr/8/8/PPPPPPPP/PPPPPPPP/8/8/3qk3 w KQkq - 0 1'
    const [position, setPosition] = useState(starter); // Initialize board position
    const [turn, setTurn] = useState('White'); // Track whose turn it is
    const [status, setStatus] = useState('');

    // Handle piece drop
    const onDrop = async (sourceSquare, targetSquare) => {
        const move = sourceSquare + targetSquare; // Create move string (e.g., "e2e4")
        
        try {
            const response = await fetch('http://127.0.0.1:5000/', { // Update URL for the backend
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Set content type to JSON
                },
                body: JSON.stringify({ move }), // Send move as JSON
            });

            const data = await response.json(); // Parse JSON response
            
            if (data.legal) {
                setPosition(data.position); // Update board position
                setTurn(data.turn); // Update turn
                setStatus(data.status); // Update status
            } else {
                alert('Illegal move, try again!'); // Alert for illegal moves
            }
        } catch (error) {
            console.error('Error sending move:', error);
        }
    };

    return (
        <div className="App">
            <h1>Python Chess with React</h1>
            <Chessboard position={position} onPieceDrop={onDrop} />
            <div>
                <p>Current Turn: {turn}</p>
                <p>Status: {status}</p>
            </div>
        </div>
    );
}

export default App;
