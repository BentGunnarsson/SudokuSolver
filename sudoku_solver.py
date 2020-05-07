import numpy as np
import time

custom_grid = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 3, 8, 7, 0, 9, 0],
    [0, 1, 0, 0, 0, 0, 3, 0, 8],
    [4, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 8, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 3, 0, 0, 9, 0, 4, 7],
    [6, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 2, 7, 1, 6, 0, 0, 0, 0],
]

basic_grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

zero_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def valid(grid, x, y, num):
    for i in range(9):
        if grid[y][i] == num:
            return False
        if grid[i][x] == num:
            return False

    x_box = (x // 3) * 3
    y_box = (y // 3) * 3  

    for i in range(3):
        for j in range(3):
            if grid[y_box + i][x_box + j] == num:
                return False
    return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if valid(grid, x, y, n):
                        grid[y][x] = n
                        print(np.matrix(grid))
                        print()
                        time.sleep(0.001)
                        solve(grid)
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    yes_or_no = input("More? (y/n) ")
    if yes_or_no == "n":
        print("Done!")
        quit()
    
def solver(grid):
    print("Solving the sudoku puzzle..")
    solve(grid)

def main_menu(grid):
    print("You chose to solve this puzzle!")
    print(np.matrix(grid))
    time.sleep(2)
    print("Let's go!")
    time.sleep(1)
    solver(grid)

def main():
    print("Which would you like..")
    num = input("Press 1 to test a basic sudoku puzzle.\nPress 0 to solve a 0 matrix sudoku puzzle!\nPress 2 for your own custom puzzle\n")
    try:
        int_num = int(num)
    except ValueError:
        print("Numbers only..")
    if int_num == 1:
        main_menu(basic_grid)
    elif int_num == 2:
        main_menu(custom_grid)
    elif int_num == 0:
        main_menu(zero_grid)
    else:
        print("Invalid")

    main()

main()