import math


def cavityMap(grid):
    # Write your code here
    temp_grid = []
    for i in range(len(grid)):
        temp_grid.append(list(map(int, grid[i])))

    rows = len(temp_grid)
    columns = len(temp_grid[0])
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            if (temp_grid[i - 1][j] == 'X' or temp_grid[i + 1][j] == 'X' or temp_grid[i][j - 1] == 'X' or temp_grid[i][j + 1] == 'X'):
                continue
            elif temp_grid[i][j] > max(temp_grid[i - 1][j], temp_grid[i + 1][j], temp_grid[i][j - 1], temp_grid[i][j + 1]):
                temp_grid[i][j] = 'X'

    grid = []
    for i in range(rows):
        grid.append(''.join(map(str, temp_grid[i])))
    return grid


grid = ['1112', '1912', '1892', '1234']
print(cavityMap(grid))  # ['1112', '1X12', '18X2', '1234']
