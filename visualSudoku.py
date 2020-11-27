import pygame

# Colours
WHITE = 255, 255, 255
GREY = 192, 192, 192
DARKGREY = 96, 96, 96
BLACK = 0, 0, 0

# Frames per second
FPS = 144

# Initialising pygame
pygame.init()
pygame.display.set_caption("Sudoku Solver")
numbers = pygame.font.SysFont("robotocondensed", 50)

# Window size and customisable variable initialisation
boarder_width = 12
grid_space = 4
width_height = 200
screen = pygame.display.set_mode((9*width_height+2*boarder_width+8*grid_space,
                                  9*width_height+2*boarder_width+8*grid_space))


def possible(x, y, n, board):
    if any([board[x][i] == n for i in range(9)]): return False
    if any([board[i][y] == n for i in range(9)]): return False
    if any([board[((x//3)*3)+i][((y//3)*3)+j] == n for i in range(3) for j in range(3)]): return False
    return True


def solve(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n, board):
                        board[x][y] = n
                        # Draw board with pygame
                        draw(board, x, y)
                        solve(board)
                        board[x][y] = 0
                return
    # Make text green when complete
    for i in range(9):
        for j in range(9):
            screen.blit(numbers.render(str(board[j][i]), True, (0, 120, 0)), (
                i * width_height + 1 * boarder_width + i * grid_space + 0.5 * width_height - 10,
                j * width_height + 1 * boarder_width + j * grid_space + 0.5 * width_height - 16))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    input("More solutions?")


def draw(board, x, y):
    # Boarder
    screen.fill(BLACK)
    # Board background
    pygame.draw.rect(screen, GREY, [boarder_width, boarder_width,
                                    9 * width_height + 0 * boarder_width + 8 * grid_space,
                                    9 * width_height + 0 * boarder_width + 8 * grid_space])
    # Grid
    for row in range(9):
        for column in range(9):
            pygame.draw.rect(screen, WHITE, [(grid_space + width_height) * column + boarder_width,
                                             (grid_space + width_height) * row + boarder_width,
                                             width_height, width_height])
    # Thicker grid lines
    pygame.draw.line(screen, GREY, (boarder_width, 3 * width_height + 1 * boarder_width + 2 * grid_space),
                     (9 * width_height + 1 * boarder_width + 8 * grid_space - 1,
                      3 * width_height + 1 * boarder_width + 2 * grid_space), grid_space * 2)
    pygame.draw.line(screen, GREY, (boarder_width, 6 * width_height + 1 * boarder_width + 5 * grid_space),
                     (9 * width_height + 1 * boarder_width + 8 * grid_space - 1,
                      6 * width_height + 1 * boarder_width + 5 * grid_space), grid_space * 2)
    pygame.draw.line(screen, GREY, (3 * width_height + 1 * boarder_width + 2 * grid_space, boarder_width),
                     (3 * width_height + 1 * boarder_width + 2 * grid_space,
                      9 * width_height + 1 * boarder_width + 8 * grid_space - 1), grid_space * 2)
    pygame.draw.line(screen, GREY, (6 * width_height + 1 * boarder_width + 5 * grid_space, boarder_width),
                     (6 * width_height + 1 * boarder_width + 5 * grid_space,
                      9 * width_height + 1 * boarder_width + 8 * grid_space - 1), grid_space * 2)
    # Numbers
    for i in range(9):
        for j in range(9):
            if board[j][i] != 0:
                screen.blit(numbers.render(str(board[j][i]), True, (43, 43, 43)), (
                    i * width_height + 1 * boarder_width + i * grid_space + 0.5 * width_height - 10,
                    j * width_height + 1 * boarder_width + j * grid_space + 0.5 * width_height - 16))
    # row/column highlights
    c = pygame.Surface((width_height, 9 * width_height + 8 * grid_space))
    r = pygame.Surface((9 * width_height + 8 * grid_space, width_height))
    c.fill((43, 43, 43))
    r.fill((43, 43, 43))
    c.set_alpha(40)
    r.set_alpha(40)
    screen.blit(c, (y * width_height + 1 * boarder_width + y * grid_space, boarder_width))
    screen.blit(r, (boarder_width, x * width_height + 1 * boarder_width + x * grid_space))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


def main(board):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        solve(board)


#main(grid2)
