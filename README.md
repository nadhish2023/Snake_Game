# Snake Game

A classic Snake Game built using Python's `turtle` module. This project features a fully functional snake game with a high-score tracking system, obstacles (walls), and customizable controls.

---

## Features
- Dynamic snake movement with collision detection.
- Scoring system with a persistent high score.
- Customizable gameplay area and graphics.
- Supports both arrow keys and WASD controls.

---

## How to Run the Game

### Prerequisites
1. **Python**: Ensure Python 3.8 or later is installed.
2. **Turtle Graphics**: Python's `turtle` module is part of the standard library and comes pre-installed.

### Steps
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the game using the following command:
   ```
   python main.py
   ```

---

## Game Controls
- Arrow Keys (Up, Down, Left, Right)
- WASD Keys (`W`, `A`, `S`, `D`)

---

## File Structure
- `main.py`: The main driver script for the game.
- `snake.py`: Contains the `Snake` class with all snake-related logic.
- `food.py`: Contains the `Food` class to handle food generation and placement.
- `wall.py`: Handles the creation of the boundary walls.
- `highscore.py`: Manages reading and writing the high score.
- `highscore.txt`: Stores the highest score achieved.
- `image1.gif`: Background image for the game (must be in the project directory).

---

## Game Rules
1. Use the controls to move the snake and eat the red food.
2. Each food increases your score by 5 points.
3. The game ends if:
   - The snake collides with itself.
   - The snake hits the walls.

---

## Credits
This project was created using Python's `turtle`, `random`, and `time` modules.

---

## Future Enhancements
- Add multiple levels with increasing difficulty.
- Introduce power-ups or obstacles.
- Enable multiplayer functionality.

---
