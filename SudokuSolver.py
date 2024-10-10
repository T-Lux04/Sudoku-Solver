# Example Sudoku grid
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(grid, row, col, num):
    # Check if num is in the current row
    if num in grid[row]:
        return False
    # Check if num is in the current column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check if num is in the current 3*3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

def find_empty(grid):
# Find the next empty cell
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

# BackingTracking algorithm
def solve_sudoku(grid):
    # Find empty cell
    empty = find_empty(grid)
    
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        # Check if the number is valid
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            #recusive algorithm to solve the sudoku
            if solve_sudoku(grid):
                return True
        # If placing the number didnt lead to solving the problem back track
        grid[row][col] = 0

    return False  # Triggers backTrack

def print_sudoku(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

if solve_sudoku(sudoku_grid):
    print("Solved Sudoku puzzle!!!!")
    print_sudoku(sudoku_grid)
else:
    print("No solution :(")