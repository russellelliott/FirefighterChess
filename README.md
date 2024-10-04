# Firefighter Chess
Source video: https://www.youtube.com/watch?v=JqdnPCEvvqY

## Given Rules
In this variant, one player controls a firefighter and their firehose.

### Firefighter
- Starting position: e1
- Movement: King
- Attack: None; only firehose can capture fire.

### Firehose
- Starting position: d1
- Movement
    - Moves with the firefighter if they go up, down, left, right
    - Can move the firehose around the firefighter.
- Attack: Has queen attacks. Can capture multiple fire pieces along its attack path.

### Fire
- Starting positions: a4-h5 (16 pieces along ranks 4 and 5)
- Movement: Pawn movement. 2 pieces moved per turn.
- Attack: Pawn captures. Can only be captured by firehose attack. Can be jumped over.

### Victims
- Starting positions: h1-h7 (back rank royal pieces)
- Movement: regular piece movement
- Attack: None; only firehose can capture fire.

## Goal
The game ends in any of these conditions:
- Firefighter: extinguish all the fire
- Fire: Capture ANY of the victim pieces
- Victims: Evade capture and have all pieces reach the other site of the board

The firefighter and victims are on the same team.

## Implementation
The firefighter and victims are one color, while the fire is the opposite color.

### Starting movement
For fairness and consistency, fire always goes first.
- It would be unfair for the firefighter to start first as they can destroy 2 fire right away.
- If the victim pieces move first, that would give then extra time to prepare/escape. Also unfair against fire.

### Movement Types

#### Firefighter
The firefighter can make one of three move types
1. Move up, down, left or right
2. Move the hose to any of the spaces around them
3. Activate the firehose to destroy all fire in the attack line of the queen (horizontal, vertical, or diagonal)

#### Victims
Can move one of their pieces towards "White's side" avoiding the fire

#### Fire
Fire can move two of their pawns in one turn. Moves towards the victim pieces

### Player count
The game could be played with 2 or 3 players.

#### 2 Players
- Player 1 controls the firefighter and their hose, and all the victim pieces.
- Player 2 controls the fire pieces.

#### 3 Players
- Player 1 controls the firefighter and their hose.
- Player 2 controls the fire pieces.
- Player 3 controls the victim pieces.

## Architecture
Frontend: `react-chess` for drag and drop chess board

Backend: Flask Backend with Python `chess` library. This allows for more flexible board arrangements that wouldn't otherwise be legal in `chess.js`

## Running App
Frontend: go to root folder of react app and run `npm run start`

Backend: go to backend folder and run `python 3 main.py`