# Sudoku-Algorithmic-Solver

This project presents an algorithmic Sudoku solver developed in Python. The main objective is to implement and compare different optimization algorithms to solve Sudoku puzzles for different difficulties (Easy, Medium, Hard & Expert).

## Algorithms Implemented

  **Backtracking**: A standard depth-first search algorithm that tests all possible combinations recursively to find the solution.

  **Branch and Bound**: An optimized approach that prunes the search tree to reduce memory consumption and execution time, proving highly effective for complex grid constraints.

## Project Structure

*'\src'*: Contains the main source code ('main.py', 'solver_backtracking.py', 'solver_branchbound.py', 'sudoku.py' and 'utils.py').

*'\levels'*: Text files containing Sudoku matrices categorized by difficulty.

*'\report'*: Contains the detailed theoretical analysis and algorithmic breakdown ('project_report.pdf')

## Example Output
```text
```text
Original Sudoku (expert):

---------------------
| 0 0 0 | 0 0 3 | 0 1 7 
| 0 1 5 | 0 0 9 | 0 0 8 
| 0 6 0 | 0 0 0 | 0 0 0 
---------------------
| 1 0 0 | 0 0 7 | 0 0 0 
| 0 0 9 | 0 0 0 | 2 0 0 
| 0 0 0 | 5 0 0 | 0 0 4 
---------------------
| 0 0 0 | 0 0 0 | 0 2 0 
| 5 0 0 | 6 0 0 | 3 4 0 
| 3 4 0 | 2 0 0 | 0 0 0 
---------------------

Sudoku solved (backtracking):

---------------------
| 2 9 4 | 8 6 3 | 5 1 7 
| 7 1 5 | 4 2 9 | 6 3 8 
| 8 6 3 | 7 5 1 | 4 9 2 
---------------------
| 1 5 2 | 9 4 7 | 8 6 3 
| 4 7 9 | 3 8 6 | 2 5 1 
| 6 3 8 | 5 1 2 | 9 7 4 
---------------------
| 9 8 6 | 1 3 4 | 7 2 5 
| 5 2 1 | 6 7 8 | 3 4 9 
| 3 4 7 | 2 9 5 | 1 8 6 
---------------------

Puzzle solved (branch&bound):

---------------------
| 2 9 4 | 8 6 3 | 5 1 7 
| 7 1 5 | 4 2 9 | 6 3 8 
| 8 6 3 | 7 5 1 | 4 9 2 
---------------------
| 1 5 2 | 9 4 7 | 8 6 3 
| 4 7 9 | 3 8 6 | 2 5 1 
| 6 3 8 | 5 1 2 | 9 7 4 
---------------------
| 9 8 6 | 1 3 4 | 7 2 5 
| 5 2 1 | 6 7 8 | 3 4 9 
| 3 4 7 | 2 9 5 | 1 8 6 
---------------------
```
## Algorithmic Conclusions

While standard Backtracking is straightforward and easy to implement, Branch and Bound presents a significantly more efficient approach for complex scenarios. 

## Additional Notes

To execute the solver, run the main script from the root directory: 'python src/main.py'

*This project was done as a final project for the subject 'Programming 2' of Bachelor in Data Science and Engineering
at CEU University.*




