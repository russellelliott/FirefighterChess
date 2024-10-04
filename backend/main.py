from flask import Flask, request, render_template, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

CORS(app)  # Enable CORS for the app

import chess
import chess.svg
from markupsafe import Markup

starter = 'rnbqkbnr/8/8/PPPPPPPP/PPPPPPPP/8/8/3qk3 w KQkq - 0 1'
board = chess.Board(starter)

# Function to make the board
def makeBoard(FEN=starter):
    board = chess.Board(FEN)
    svg = chess.svg.board(board, size=350)  # Make the svg
    return svg

# Display homepage
@app.route('/')
def home(board=chess.Board(starter)):
    svg = chess.svg.board(board, size=350)  # Make the svg
    return render_template('index.html', svg=Markup(svg), turn="white", status="")

# Function that allows a human player to make a move
def human(board, moveInput):
    if moveInput == "":
        print("need to input valid move")
        return board
    move = chess.Move.from_uci(moveInput)  # Make the move
    if move in board.legal_moves:  # If the move is legal
        board.push(move)  # Push the move
    elif chess.Move.from_uci(moveInput + "q") in board.legal_moves:  # Check if promotion
        moveInput += 'q'  # Auto-promote to queen
        move = chess.Move.from_uci(moveInput)  # Make the move
        board.push(move)  # Push the move
    else:
        print("invalid move. try again")
    return board

# Function to check whose turn it is
def getTurn(board):
    return "white" if board.turn else "black"

# Function to check the status of the game
def getStatus(board):
    status = ""  # Default status
    if board.is_check():
        status = "check"
    if board.is_checkmate():
        status = "checkmate"
    if board.is_stalemate():
        status = "stalemate"
    return status

# Handle move requests
@app.route('/', methods=['POST', 'GET'])
def result():
    output = request.json  # Get JSON data from the request
    move = output["move"]  # Extract the move
    global board  # Make the board a global variable
    board = human(board, move)  # Update the board
    svg = chess.svg.board(board, size=350)  # Make the svg
    turn = getTurn(board)  # Get current turn
    status = getStatus(board)  # Get game status
    return jsonify({
        "legal": True,  # Indicate that the move was legal
        "position": board.fen(),  # Send updated position as FEN string
        "turn": turn,  # Send current turn
        "status": status  # Send current status
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run Flask app
