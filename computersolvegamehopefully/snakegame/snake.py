import pygame
import random
import solver

pygame.init()

winx = 1920
winh = 1080

pygame.display.set_caption("SNEK GO WEEEE")
screen = pygame.display.set_mode((winx, winh), pygame.FULLSCREEN)

sim_speed = 10
clock = pygame.time.Clock()
grid_dimensions = 800
grid_size = 4
unitsize = grid_dimensions//grid_size
offsetgrid = (screen.get_height()-grid_dimensions)/2

bg1 = pygame.Color(10, 10, 10)
bg2 = pygame.Color(20, 20, 20)
black = pygame.Color(0, 0, 0)
snekcol1 = pygame.Color(108, 186, 60)
snekcol2 = pygame.Color(54, 93, 30)
red = pygame.Color(221, 21, 51)

run=True
dir = 1 # 0-up, 1-right, 2-down, 3-left

snake = [[0, 0], [1, 0]]

spots = []

gridcombs = []
for y in range(grid_size):
    for x in range(grid_size):
        gridcombs.append([x, y])

for i in gridcombs:
    if i not in snake:
        spots.append(i)
apple = random.choice(spots)

def CalculateColor(rgb1, rgb2:pygame.Color, a1, a2):
    r = rgb2.r+((rgb1.r-rgb2.r)*a1/a2)
    g = rgb2.g+((rgb1.g-rgb2.g)*a1/a2)
    b = rgb2.b+((rgb1.b-rgb2.b)*a1/a2)
    return pygame.Color(round(r), round(g), round(b))

solver = solver.SolvingAlgorithms(grid_size, gridcombs)

while run:
    solver.solve(snake, apple)
    dir = solver.DirectionToTravel

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != 2:
                dir = 0
            if event.key == pygame.K_DOWN and dir != 0:
                dir = 2
            if event.key == pygame.K_LEFT and dir != 1:
                dir = 3
            if event.key == pygame.K_RIGHT and dir != 3:
                dir = 1

    #logic
    snakepos = snake[len(snake)-1]
    new_block = [0, 0]
    if dir==0:
        new_block = [snakepos[0], snakepos[1]-1]
    elif dir==1:
        new_block = [snakepos[0]+1, snakepos[1]]
    elif dir==2:
        new_block = [snakepos[0], snakepos[1]+1]
    elif dir==3:
        new_block = [snakepos[0]-1, snakepos[1]]

    if -1 in new_block or grid_size in new_block or snake[len(snake)-1] in snake[:-1]:
        run=False
        break

    if snake[len(snake)-1] == apple:
        spots = []
        for i in gridcombs:
            if i not in snake:
                spots.append(i)
        apple = random.choice(spots)
    else:
        snake.pop(0)

    snake.append(new_block)

    # render
    screen.fill(black)
    blitusingbg1=True
    for y in range(grid_size):
        for x in range(grid_size):
            pygame.draw.rect(screen, bg1 if blitusingbg1 else bg2, [offsetgrid+(unitsize*x), offsetgrid+(unitsize*y), unitsize, unitsize])
            if [x, y] in snake:
                pygame.draw.rect(screen, CalculateColor(snekcol1, snekcol2, snake.index([x, y]), len(snake)), [offsetgrid+(unitsize*x), offsetgrid+(unitsize*y), unitsize, unitsize])
            elif [x, y] == apple:
                pygame.draw.rect(screen, red, [offsetgrid+(unitsize*x), offsetgrid+(unitsize*y), unitsize, unitsize])
            blitusingbg1=not blitusingbg1
        blitusingbg1=not blitusingbg1
    pygame.display.flip()
    clock.tick(sim_speed)

pygame.quit()
quit()
