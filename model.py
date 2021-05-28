# 12.1.2020: Young Rafey, you really sucked at code documentation I'm highly
# irritated at you -_-
# program created circa Jun/Jul 2019

import random
import view

height = 100
width = 100

def randomize(grid, height, width):
    """Function generates random values for each cell in grid.
    """
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0, 1)

# creates array rows
main_grid = [0] * height
next_grid = [0] * height

# so um this makes the grid I guess? ugh. no actually. idk.
# OH I think I'm building a 2D array here - each array element from previous
# contains an array itself. 
for i in range(height):                 
    main_grid[i] = [0] * width
    next_grid[i] = [0] * width

def next_gen():
    """Function generates next generation of cells.
    """
    global main_grid, next_grid

    for i in range(0, height):
        for j in range(0, width):
            cell = 0
            count = count_neighbors(main_grid, i, j)
            
            if main_grid[i][j] == 0 and count == 3:
                cell = 1
            elif (main_grid[i][j] == 1) and (count == 2 or count == 3):
                cell = 1
            next_grid[i][j] = cell

    temp = main_grid
    main_grid = next_grid
    next_grid = temp
            
def count_neighbors(grid, row, col):
    """Function checks status of adjacent boxes in grid to count neighboring
       cells. Each cell has value of 0 or 1.
    """
    count = 0
    if row - 1 >= 0:
        count = count + grid[row-1][col]
    if (row - 1 >= 0) and (col - 1 >= 0):
        count = count + grid[row-1][col-1]
    if (row - 1 >= 0) and (col + 1 < width):
        count = count + grid[row-1][col+1]
    if col - 1 >= 0:
        count = count + grid[row][col-1]
    if col + 1 < width:
        count = count + grid[row][col+1]
    if row + 1 < height:
        count = count + grid[row+1][col] 
    if (row + 1 < height) and (col - 1 >= 0):
        count = count + grid[row+1][col-1]        
    if (row + 1 < height) and (col + 1 < width):
        count = count + grid[row+1][col+1]

    return count

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def load_pattern(pattern, x_offset = 0, y_offset = 0):
    global main_grid

    for i in range(0, height):
        for j in range(0, width):
            main_grid[i][j] = 0

    j = y_offset

    for row in pattern:
        i = x_offset
        for value in row:
            main_grid[i][j] = value
            i = i + 1
        j = j + 1

if __name__ == "__main__":
    next_gen()
    
