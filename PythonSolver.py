import pygame

WIDTH = 600
HEIGHT = 800
GRID = 9

######################################################################################################################################
class Box():
    def __init__(self):
        self.x = WIDTH/GRID

######################################################################################################################################
def findEmpty(grid):

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return (i, j)  # row, col

######################################################################################################################################
#row, col
def possible(y, x, num, grid):
    for i in range(len(grid)):
        if grid[y][i] == num or grid[i][x] == num:
            return False

    y0 = (y//3)*3
    x0 = (x//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == num:
                return False

    return True


######################################################################################################################################
def solve(grid):
    find = findEmpty(grid)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1,len(grid) + 1):
        if possible(row, col, num, grid):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

######################################################################################################################################

def printMat(grid):
    for row in range(0,9):
        for col in range(0,9):
            print(grid[row][col], end = ' ')
        print("\n")

######################################################################################################################################
def getGrid():
    return [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0], 
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

######################################################################################################################################
def main():

    pygame.init()
    pygame.display.set_caption("Sudoku")
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    board = (10, 10, WIDTH, WIDTH)
    pygame.draw.rect(win, (0,0,0), board)
    pygame.display.update()

    grid = getGrid()

    printMat(grid)
    print()
    solve(grid)
    printMat(grid)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

######################################################################################################################################

main()