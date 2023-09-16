import tkinter as tk

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            entry = entries[i][j]
            entry.delete(0, tk.END)
            entry.insert(0, str(grid[i][j]))

def is_valid_move(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True

    row, col = empty_loc

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def solve():
    user_grid = [[int(entries[i][j].get()) for j in range(9)] for i in range(9)]

    if solve_sudoku(user_grid):
        print_grid(user_grid)
    else:
        result_label.config(text="Aucune solution n'existe pour cette grille.")

def clear():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Solveur de sudoku")

# Create entry widgets for Sudoku grid
entries = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j] = tk.Entry(root, width=3, font=('Arial', 16), justify="center")
        entries[i][j].grid(row=i, column=j, padx=2, pady=2)
        # Ajouter une ligne de grille pour mettre en évidence les carrés de 3x3
        if i % 3 == 0:
            entries[i][j].grid(pady=(5, 0))
        if j % 3 == 0:
            entries[i][j].grid(padx=(5, 0))

# Create Solve and Clear buttons
solve_button = tk.Button(root, text="Résoudre", command=solve)
solve_button.grid(row=10, column=0, columnspan=4, pady=10)
clear_button = tk.Button(root, text="Effacer", command=clear)
clear_button.grid(row=10, column=5, columnspan=4, pady=10)

# Create a label for the result
result_label = tk.Label(root, text="", fg="red")
result_label.grid(row=11, column=0, columnspan=9)

root.iconbitmap('icon.ico')
root.mainloop()
