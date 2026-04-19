# COM103 Midterm Exam – Mobile Legends Match Log

This Python program records up to 4 Mobile Legends matches, calculates each match's KDA, classifies performance based on results, counts wins/losses, and identifies the best match.

## Features
- Hardcoded hero roster with roles
- Calculates KDA: (kills + assists) / deaths
- Handles divide-by-zero safely
- Performance tags:
  - KDA ≥ 5 and Win → DOMINATION!
  - KDA < 5 and Loss → Better Luck Next Game
- Win rate calculation and best match summary

## How to Run
1. Clone this repository.
2. Open the terminal in the project folder.
3. Run:
   ```bash
   python midterm_solution.py
