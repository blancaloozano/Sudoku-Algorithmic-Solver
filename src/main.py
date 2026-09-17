from utils import load_puzzle
from utils import print_puzzle
from sudoku import Sudoku
from solver_backtracking import solve_backtracking
from solver_branchbound import solve_branchbound
import time


def main():

    valid_levels = {"easy", "medium", "hard", "expert"}

    level = input("\nWhat level do you want?\nOptions: Easy, Medium, Hard, Expert\n").strip().lower()

    if level not in valid_levels:
        print("Invalid level. Try again")
        return


    filepath = f"levels/{level}.txt"

    puzzle = load_puzzle(filepath)
    print(f"\nOriginal Sudoku ({level}):\n")
    print(print_puzzle(puzzle))

    sudoku = Sudoku(puzzle)

    start_time_bt = time.time()
    solved_bt = solve_backtracking(sudoku)
    end_time_bt = time.time()

    if solved_bt:
        exec_time_bt = end_time_bt - start_time_bt
        print(f"\nSudoku solved (backtracking) | Execution time: {exec_time_bt:.5f} s\n")
        print(print_puzzle(sudoku.puzzle))
    else:
        print("There's no solution for this puzzle")


    puzzle2 = load_puzzle(filepath)
    sudoku2 = Sudoku(puzzle2)

    start_time_bb = time.time()
    solved_bb = solve_branchbound(sudoku2)
    end_time_bb = time.time()

    if solved_bb:
        exec_time_bb = end_time_bb- start_time_bb 
        print(f"\nPuzzle solved (branch&bound) | Execution time: {exec_time_bb:.5f} s\n")
        print(print_puzzle(sudoku.puzzle))
    else:
        print("There's no solution for this puzzle")


if __name__ == "__main__":
    main()