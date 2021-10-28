from random import randrange

import pygame as pg

SIZE = 100
MAX_PILE = 4
CASE = 5
WIDTH, HEIGHT = SIZE * CASE, SIZE * CASE
R = 255 // MAX_PILE + 1
COLORS = [(255 - i * R, 255 - i * R, 255 - i * R) for i in range(MAX_PILE)] + [
    (0, 0, 0)
]
MAX_ITERATIONS = 100000
to_slide: list[tuple[int, int]] = []

pg.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
pg.display.set_caption("Sandpile Simulation")
SCREEN.fill(COLORS[0])
pg.display.update()

grid = []
for i in range(SIZE):
    line = []
    for j in range(SIZE):
        line.append(0)
    grid.append(line)


def is_in_bound(x: int, y: int) -> bool:
    if 0 > x or x >= SIZE or 0 > y or y >= SIZE:
        return False
    else:
        return True


def dessiner(x: int, y: int) -> None:
    pg.draw.rect(SCREEN, COLORS[grid[x][y]], (x * CASE, y * CASE, CASE, CASE))
    # pg.display.update()


for iteration in range(MAX_ITERATIONS):
    longueur = len(to_slide)
    if longueur == 0:
        x = randrange(0, SIZE)
        y = randrange(0, SIZE)

        grid[x][y] += 1
        if grid[x][y] == MAX_PILE:
            grid[x][y] = 0
            to_slide.append((x - 1, y))
            to_slide.append((x + 1, y))
            to_slide.append((x, y + 1))
            to_slide.append((x, y - 1))
        dessiner(x, y)
    else:
        for i in range(longueur):
            x, y = to_slide.pop(0)
            if is_in_bound(x, y):
                if grid[x][y] < MAX_PILE:
                    grid[x][y] += 1
                if grid[x][y] == MAX_PILE:
                    grid[x][y] = 0
                    to_slide.append((x - 1, y))
                    to_slide.append((x + 1, y))
                    to_slide.append((x, y + 1))
                    to_slide.append((x, y - 1))
                dessiner(x, y)
            pg.display.update()
    pg.display.set_caption(f"Itération n°{iteration}")
