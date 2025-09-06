
# DAA Sorting Game - Django Web App

## Overview

This project is a web-based interactive game designed to teach and demonstrate sorting algorithms. Built with Django, it allows users to play, learn, and reflect on algorithmic thinking through hands-on gameplay.

## Game Features

- **Sorting Algorithms:** Bubble Sort, Selection Sort, Insertion Sort
- **Interactive Gameplay:** Click-to-select and swap elements, visual feedback for correct/incorrect moves, game ends with a winning overlay when sorting is complete
- **Difficulty Levels:** Easy (5–15 elements), Medium (16–30 elements), Hard (31–50 elements)
- **Game Persistence:** Save and resume games, view history of saved games
- **Learning Resources:** Dedicated “Learn” page with detailed explanations, step-by-step examples, pseudocode, and visual animations for each algorithm

## Design & Algorithmic Logic

- **Game Logic:** Each sorting algorithm enforces its own rules for valid moves. The game validates each move and provides instant feedback. The game state is saved in the database, allowing users to resume or review their progress.
- **Algorithms Implemented:**
	- **Bubble Sort:** Only adjacent swaps allowed; must move larger element right.
	- **Selection Sort:** Select minimum in unsorted portion and swap with first unsorted position.
	- **Insertion Sort:** Insert next unsorted element into correct position in sorted portion.
- **Creativity & Critical Thinking:** The game uses playful UI/UX, themed backgrounds, and a winning overlay for engagement. The “Learn” page provides algorithmic context and visual learning.

## Setup & Requirements

### Requirements

- Python 3.8+
- Django 4.2.7

All dependencies are listed in `requirements.txt`:
```
Django==4.2.7
```
No other external packages are required.

### Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Usage

- Visit the home page to start or resume a game.
- Select an algorithm and difficulty, then play by swapping elements according to the rules.
- Use hints if stuck.
- When the array is sorted, a winning overlay appears.
- Visit the “Learn” page for algorithm explanations.

## File Structure

- `manage.py` — Django project manager
- `requirements.txt` — Project dependencies
- `game/` — Main Django app
	- `models.py` — Game state model
	- `views.py` — Game logic and API endpoints
	- `templates/game/` — HTML templates for home, game, learn, and resume pages
	- `migrations/` — Database migrations

## Reflection

- **Conceptual Understanding:** The game enforces algorithmic rules, helping users internalize sorting logic through play.
- **Creativity:** Themed UI, interactive feedback, and a dedicated learning page make the experience engaging.
- **Algorithmic Thinking:** Players must think critically about each move, applying the logic of the chosen algorithm.

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home1.png)
![Home Page](screenshots/home2.png)

### Game Screen
![Game Screen](screenshots/game1.png)
![Game Screen](screenshots/game2.png)

### Resume Game
![Resume Game](screenshots/resume1.png)

### Learn Page
![Learn Page](screenshots/learn1.png)
![Learn Page](screenshots/learn2.png)

