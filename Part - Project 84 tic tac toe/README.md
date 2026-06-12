# Tic Tac Toe Game

## Project Overview
A complete Tic Tac Toe game implementation with both two-player mode and AI opponent using the Minimax algorithm. This command-line game features intelligent computer play, game state management, and a clean user interface.

## Technologies Used
- Python 3.x
- Standard library only (no external dependencies)
- Minimax algorithm with alpha-beta pruning
- Command-line interface
- Game state management

## Project Structure
```
Part - Project 84 tic tac toe/
├── ticTacToe.py        # Complete Tic Tac Toe game
└── README.md           # This file
```

## Features
- **Two Game Modes**: Player vs Player and Player vs AI
- **Intelligent AI**: Uses Minimax algorithm for optimal play
- **Game Board Display**: Clear ASCII representation of the board
- **Input Validation**: Prevents invalid moves
- **Win Detection**: Checks all possible winning combinations
- **Draw Detection**: Identifies when the board is full
- **Game Statistics**: Tracks wins, losses, and draws
- **Replay Option**: Play multiple games in one session

## Installation
No installation required! This is a standalone Python script:
```bash
# Simply run the script
python ticTacToe.py
```

## How to Play
1. Run the script:
   ```bash
   python ticTacToe.py
   ```
2. Choose game mode:
   - `1` for Player vs Player
   - `2` for Player vs AI
3. Enter moves by number (1-9) corresponding to board positions:
   ```
    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9
   ```
4. Players take turns until someone wins or the game ends in a draw
5. Option to play again or exit

## Game Rules
- **Players**: X (always goes first) and O
- **Objective**: Get three of your marks in a row (horizontal, vertical, or diagonal)
- **Turns**: Players alternate turns
- **Board**: 3x3 grid
- **Winning Combinations**: 8 possible winning lines
- **Draw**: Board filled with no winner

## Code Structure
### Game Constants
```python
WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6),             # Diagonals
]
```

### Board Management
```python
def create_board():
    """Create an empty game board."""
    return [" "] * 9

def display_board(board):
    """Display the current game board."""
    def cell(i):
        return board[i] if board[i] != " " else str(i + 1)
    
    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()
```

### Game Logic
```python
def has_winner(board, player):
    """Check if a player has won."""
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in WIN_COMBINATIONS
    )

def board_full(board):
    """Check if the board is completely filled."""
    return " " not in board

def valid_move(board, position):
    """Validate if a move is legal."""
    if position < 1 or position > 9:
        return False
    return board[position - 1] == " "
```

## AI Implementation (Minimax Algorithm)
### Minimax with Alpha-Beta Pruning
```python
def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm with alpha-beta pruning for optimal AI moves."""
    # Terminal states
    if has_winner(board, "X"):
        return -10 + depth  # Prefer earlier wins
    if has_winner(board, "O"):
        return 10 - depth   # Prefer earlier wins for AI
    if board_full(board):
        return 0
    
    if is_maximizing:  # AI's turn (O)
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cutoff
        return best_score
    else:  # Player's turn (X)
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cutoff
        return best_score

def get_ai_move(board):
    """Get the best move for the AI using Minimax."""
    best_score = -float('inf')
    best_move = -1
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = " "
            
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move + 1  # Convert to 1-9 position
```

## Game Modes
### Player vs Player Mode
```python
def play_two_player():
    """Two human players game mode."""
    board = create_board()
    current_player = "X"
    
    while True:
        display_board(board)
        
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): "))
            
            if not valid_move(board, move):
                print("Invalid move. Try again.")
                continue
            
            board[move - 1] = current_player
            
            # Check for winner
            if has_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                return current_player
            
            # Check for draw
            if board_full(board):
                display_board(board)
                print("It's a draw!")
                return "Draw"
            
            # Switch player
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Please enter a number between 1 and 9.")
```

### Player vs AI Mode
```python
def play_vs_ai():
    """Player vs AI game mode."""
    board = create_board()
    
    while True:
        # Player's turn
        display_board(board)
        
        try:
            move = int(input("Your turn (X), enter position (1-9): "))
            
            if not valid_move(board, move):
                print("Invalid move. Try again.")
                continue
            
            board[move - 1] = "X"
            
            # Check if player wins
            if has_winner(board, "X"):
                display_board(board)
                print("Congratulations! You win!")
                return "X"
            
            if board_full(board):
                display_board(board)
                print("It's a draw!")
                return "Draw"
            
            # AI's turn
            print("\nAI is thinking...")
            ai_move = get_ai_move(board)
            board[ai_move - 1] = "O"
            print(f"AI plays at position {ai_move}")
            
            # Check if AI wins
            if has_winner(board, "O"):
                display_board(board)
                print("AI wins! Better luck next time.")
                return "O"
            
            if board_full(board):
                display_board(board)
                print("It's a draw!")
                return "Draw"
            
        except ValueError:
            print("Please enter a number between 1 and 9.")
```

## Game Statistics
```python
class GameStats:
    """Track game statistics."""
    
    def __init__(self):
        self.wins_x = 0
        self.wins_o = 0
        self.draws = 0
        self.games_played = 0
    
    def update(self, result):
        """Update statistics based on game result."""
        self.games_played += 1
        
        if result == "X":
            self.wins_x += 1
        elif result == "O":
            self.wins_o += 1
        else:
            self.draws += 1
    
    def display(self):
        """Display current statistics."""
        print("\n=== Game Statistics ===")
        print(f"Games Played: {self.games_played}")
        print(f"Player X Wins: {self.wins_x}")
        print(f"Player O Wins: {self.wins_o}")
        print(f"Draws: {self.draws}")
        
        if self.games_played > 0:
            win_rate_x = (self.wins_x / self.games_played) * 100
            win_rate_o = (self.wins_o / self.games_played) * 100
            draw_rate = (self.draws / self.games_played) * 100
            
            print(f"\nWin Rate X: {win_rate_x:.1f}%")
            print(f"Win Rate O: {win_rate_o:.1f}%")
            print(f"Draw Rate: {draw_rate:.1f}%")
```

## Advanced AI Features
### Difficulty Levels
```python
def get_ai_move_with_difficulty(board, difficulty="hard"):
    """Get AI move based on difficulty level."""
    if difficulty == "easy":
        # Random move
        available = [i + 1 for i in range(9) if board[i] == " "]
        return random.choice(available)
    
    elif difficulty == "medium":
        # Mix of random and optimal moves
        if random.random() < 0.5:
            available = [i + 1 for i in range(9) if board[i] == " "]
            return random.choice(available)
        else:
            return get_ai_move(board)
    
    else:  # hard
        return get_ai_move(board)
```

### Opening Book
```python
OPENING_BOOK = {
    # Best responses to common openings
    "empty": [5],  # Center is best opening move
    
    # Responses to corner openings
    "1": [5, 9, 7],  # If player takes top-left
    "3": [5, 7, 9],  # If player takes top-right
    "7": [5, 3, 1],  # If player takes bottom-left
    "9": [5, 1, 3],  # If player takes bottom-right
    
    # Responses to edge openings
    "2": [5, 1, 3],  # If player takes top-center
    "4": [5, 1, 7],  # If player takes middle-left
    "6": [5, 3, 9],  # If player takes middle-right
    "8": [5, 7, 9],  # If player takes bottom-center
}

def get_opening_move(board):
    """Get opening move from opening book for faster play."""
    # Count moves to determine if we're in opening
    moves_played = 9 - board.count(" ")
    
    if moves_played <= 2:  # Only in early game
        # Convert board to opening key
        player_moves = [str(i + 1) for i in range(9) if board[i] == "X"]
        
        if player_moves:
            key = player_moves[0]  # First player move
            if key in OPENING_BOOK:
                # Try moves from opening book
                for move in OPENING_BOOK[key]:
                    if board[move - 1] == " ":
                        return move
    
    return None  # No opening book move found
```

## Game Analysis Tools
### Board Evaluation
```python
def evaluate_board(board):
    """Evaluate board state for analysis."""
    score = 0
    
    # Check each winning line
    for a, b, c in WIN_COMBINATIONS:
        line = [board[a], board[b], board[c]]
        
        # Count X and O in line
        x_count = line.count("X")
        o_count = line.count("O")
        
        # Score based on line potential
        if x_count == 3:
            score -= 100  # Player win
        elif o_count == 3:
            score += 100  # AI win
        elif x_count == 2 and o_count == 0:
            score -= 10   # Player threat
        elif o_count == 2 and x_count == 0:
            score += 10   # AI threat
        elif x_count == 1 and o_count == 0:
            score -= 1    # Player potential
        elif o_count == 1 and x_count == 0:
            score += 1    # AI potential
    
    return score
```

### Move History
```python
class MoveHistory:
    """Track game move history for analysis."""
    
    def __init__(self):
        self.moves = []
        self.board_states = []
    
    def record_move(self, board, player, position):
        """Record a move in history."""
        self.moves.append({
            'player': player,
            'position': position,
            'board': board.copy()
        })
        self.board_states.append(board.copy())
    
    def display_history(self):
        """Display move history."""
        print("\n=== Move History ===")
        for i, move in enumerate(self.moves, 1):
            print(f"Move {i}: {move['player']} at {move['position']}")
```

## Testing Framework
### Unit Tests
```python
import unittest

class TestTicTacToe(unittest.TestCase):
    
    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), 9)
        self.assertEqual(board.count(" "), 9)
    
    def test_valid_move(self):
        board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertTrue(valid_move(board, 2))
        self.assertFalse(valid_move(board, 1))
        self.assertFalse(valid_move(board, 10))
        self.assertFalse(valid_move(board, 0))
    
    def test_has_winner(self):
        # Test horizontal win
        board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(has_winner(board, "X"))
        self.assertFalse(has_winner(board, "O"))
        
        # Test vertical win
        board = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
        self.assertTrue(has_winner(board, "O"))
        
        # Test diagonal win
        board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        self.assertTrue(has_winner(board, "X"))
    
    def test_board_full(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        self.assertTrue(board_full(board))
        
        board = ["X", " ", "X", "O", "X", "O", "O", "X", "O"]
        self.assertFalse(board_full(board))

if __name__ == "__main__":
    unittest.main()
```

## Performance Optimization
### Caching Minimax Results
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def minimax_cached(board_tuple, depth, is_maximizing, alpha, beta):
    """Cached version of minimax for better performance."""
    board = list(board_tuple)
    
    # Terminal states check (same as before)
    # ... minimax logic ...
    
    return best_score
```

### Early Termination
```python
def get_quick_ai_move(board):
    """Quick AI move with early termination for faster play."""
    # Check for immediate win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if has_winner(board, "O"):
                board[i] = " "
                return i + 1
            board[i] = " "
    
    # Block opponent's immediate win
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if has_winner(board, "X"):
                board[i] = " "
                return i + 1
            board[i] = " "
    
    # Use full minimax for other cases
    return get_ai_move(board)
```

## Educational Value
### Learning Concepts Demonstrated
1. **Game Theory**: Perfect information, zero-sum game
2. **Search Algorithms**: Minimax with alpha-beta pruning
3. **State Space**: 9! possible game states (reduced by symmetry)
4. **Decision Making**: Optimal move selection
5. **Algorithm Complexity**: O(b^d) reduced by pruning
6. **Heuristic Evaluation**: Board state scoring
7. **Recursion**: Depth-first search implementation

## Project Purpose
This project demonstrates:
- Game development fundamentals
- AI algorithm implementation (Minimax)
- Recursive programming techniques
- Game state management
- User interface design for command-line
- Algorithm optimization (alpha-beta pruning)
- Testing and validation strategies
- Educational game design principles