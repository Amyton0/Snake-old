import pygame
import random
from pygame.locals import *

pygame.init()

FPS = 60
WIN_WIDTH = 1000
WIN_HEIGHT = 600
BLACK = (0, 0, 0)
GREEN = (0, 225, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 121, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
GRAY = (169, 169, 169)
GRAY1 = (240, 240, 240)
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
l = 5


def proverka(coords1, coords2, r1=10, r2=10):
    catet1 = abs(coords1[0] - coords2[0])
    catet2 = abs(coords1[1] - coords2[1])
    if catet1 ** 2 + catet2 ** 2 <= (r1 + r2) ** 2:
        return True
    return None


def play():
    global l
    catet = (20, 20, 20, 20, 20, 20, 19, 19, 19, 18, 18, 17, 16, 15, 14, 13, 12, 11, 9, 6)
    clock = pygame.time.Clock()
    turns = []
    r = 10
    x = WIN_WIDTH // 2
    y = WIN_HEIGHT // 2
    l = 5
    flag = True
    direction = 1
    n_step = 0
    sc.fill(GRAY1)
    pygame.draw.circle(sc, ORANGE, (x, y), r)
    pygame.draw.circle(sc, WHITE, (x + 4, y - 3), 3)
    pygame.draw.circle(sc, WHITE, (x - 4, y - 3), 3)
    pygame.draw.circle(sc, BLACK, (x + 4, y - 3), 1)
    pygame.draw.circle(sc, BLACK, (x - 4, y - 3), 1)
    pygame.display.update()
    food = (random.randint(r, WIN_WIDTH - r), random.randint(r, WIN_HEIGHT - r))
    enemies = [
        [random.randint(0, WIN_WIDTH - 15), random.randint(0, WIN_HEIGHT - 15)],
        [random.randint(0, WIN_WIDTH - 15), random.randint(0, WIN_HEIGHT - 15)],
        [random.randint(0, WIN_WIDTH - 15), random.randint(0, WIN_HEIGHT - 15)],
        [random.randint(0, WIN_WIDTH - 15), random.randint(0, WIN_HEIGHT - 15)],
        [random.randint(0, WIN_WIDTH - 15), random.randint(0, WIN_HEIGHT - 15)]
    ]
    enemies_directions = [1, 1, 1, 1, 1]

    for i in range(len(enemies)):
        if proverka(enemies[i], food, 15):
            enemies[i] = [random.randint(0, WIN_WIDTH - 15), random.randint(0, WIN_HEIGHT - 15)]
            continue

    f1 = pygame.font.SysFont('serif', 36)

    while True:
        sc.fill(GRAY1)
        for i in pygame.event.get():
            if i.type == QUIT:
                exit()
            if flag and i.type == KEYDOWN:
                if (i.key == K_UP or i.key == K_w) and direction % 2 == 0:
                    turns.append((x, y, direction))
                    direction = 1
                elif (i.key == K_RIGHT or i.key == K_d) and direction % 2 == 1:
                    turns.append((x, y, direction))
                    direction = 2
                elif (i.key == K_DOWN or i.key == K_s) and direction % 2 == 0:
                    turns.append((x, y, direction))
                    direction = 3
                elif (i.key == K_LEFT or i.key == K_a) and direction % 2 == 1:
                    turns.append((x, y, direction))
                    direction = 4
            if i.type == MOUSEBUTTONDOWN and i.button == 1 and proverka(i.pos, (WIN_WIDTH - 15, 15), 0, 12):
                flag = not flag
                continue

        if flag:
            xy = []
            if direction == 1:
                y -= 2
            elif direction == 2:
                x += 2
            elif direction == 3:
                y += 2
            else:
                x -= 2

            clock.tick(FPS)
            if proverka((x, y), food):
                l += 1
                food = (random.randint(r, WIN_WIDTH - r), random.randint(r, WIN_HEIGHT - r))

            pygame.display.set_caption('Змейка')
            pygame.draw.circle(sc, ORANGE, (x, y), r)
            pygame.draw.circle(sc, GREEN, food, r)
            pygame.draw.circle(sc, GRAY, (WIN_WIDTH - 15, 15), 10, 2)
            pygame.draw.rect(sc, GRAY, (WIN_WIDTH - 18, 10, 3, 10))
            pygame.draw.rect(sc, GRAY, (WIN_WIDTH - 14, 10, 3, 10))

            if direction == 1:
                pygame.draw.circle(sc, WHITE, (x - 4, y - 3), 3)
                pygame.draw.circle(sc, WHITE, (x + 4, y - 3), 3)
                pygame.draw.circle(sc, BLACK, (x + 4, y - 3), 1)
                pygame.draw.circle(sc, BLACK, (x - 4, y - 3), 1)
            elif direction == 2:
                pygame.draw.circle(sc, WHITE, (x + 3, y - 4), 3)
                pygame.draw.circle(sc, WHITE, (x + 3, y + 4), 3)
                pygame.draw.circle(sc, BLACK, (x + 3, y - 4), 1)
                pygame.draw.circle(sc, BLACK, (x + 3, y + 4), 1)
            elif direction == 3:
                pygame.draw.circle(sc, WHITE, (x - 4, y + 3), 3)
                pygame.draw.circle(sc, WHITE, (x + 4, y + 3), 3)
                pygame.draw.circle(sc, BLACK, (x + 4, y + 3), 1)
                pygame.draw.circle(sc, BLACK, (x - 4, y + 3), 1)
            else:
                pygame.draw.circle(sc, WHITE, (x - 3, y - 4), 3)
                pygame.draw.circle(sc, WHITE, (x - 3, y + 4), 3)
                pygame.draw.circle(sc, BLACK, (x - 3, y - 4), 1)
                pygame.draw.circle(sc, BLACK, (x - 3, y + 4), 1)

            for i in range(len(enemies)):
                pygame.draw.circle(sc, RED, enemies[i], 15)
                pygame.draw.circle(sc, WHITE, (enemies[i][0] - 5, enemies[i][1] - 5), 5)
                pygame.draw.circle(sc, WHITE, (enemies[i][0] + 5, enemies[i][1] - 5), 5)
                pygame.draw.circle(sc, BLACK, (enemies[i][0] - 5, enemies[i][1] - 5), 3)
                pygame.draw.circle(sc, BLACK, (enemies[i][0] + 5, enemies[i][1] - 5), 3)
                pygame.draw.rect(sc, BLACK, (enemies[i][0] - 5, enemies[i][1] + 5, 10, 3))

                if proverka(enemies[i], (x, y), 15):
                    return 1
                if n_step % 10 == 0:
                    enemies_directions[i] = random.randint(1, 5)
                if enemies_directions[i] == 1:
                    enemies[i][1] -= 2
                elif enemies_directions[i] == 2:
                    enemies[i][0] += 2
                elif enemies_directions[i] == 3:
                    enemies[i][1] += 2
                else:
                    enemies[i][0] -= 2

                if enemies[i][0] + r >= WIN_WIDTH:
                    enemies[i][0] -= WIN_WIDTH
                if enemies[i][1] + r >= WIN_HEIGHT:
                    enemies[i][1] -= WIN_HEIGHT
                if enemies[i][0] - r <= 0:
                    enemies[i][0] += WIN_WIDTH
                if enemies[i][1] - r <= 0:
                    enemies[i][1] += WIN_HEIGHT

            n_step += 1
            turns_copy = turns[:]
            x1 = x
            y1 = y
            direction1 = direction

            for i in range(l - 1):
                if turns_copy:
                    if direction1 == 1:
                        a = y1 + 2 * r
                        y2 = y1
                        y1 = turns_copy[-1][1]
                        if 2 * r <= abs(y1 - y2):
                            y1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 2:
                                x1 -= catet[int(abs(y1 - y2))]
                            else:
                                x1 += catet[int(abs(y1 - y2))]
                    elif direction1 == 2:
                        a = x1 - 2 * r
                        x2 = x1
                        x1 = turns_copy[-1][0]
                        if 2 * r <= abs(x1 - x2):
                            x1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 1:
                                y1 += catet[int(abs(x1 - x2))]
                            else:
                                y1 -= catet[int(abs(x1 - x2))]
                    elif direction1 == 3:
                        a = y1 - 2 * r
                        y2 = y1
                        y1 = turns_copy[-1][1]
                        if 2 * r <= abs(y1 - y2):
                            y1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 2:
                                x1 -= catet[int(abs(y1 - y2))]
                            else:
                                x1 += catet[int(abs(y1 - y2))]
                    else:
                        a = x1 + 2 * r
                        x2 = x1
                        x1 = turns_copy[-1][0]
                        if 2 * r <= abs(x1 - x2):
                            x1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 1:
                                y1 += catet[int(abs(x1 - x2))]
                            else:
                                y1 -= catet[int(abs(x1 - x2))]
                elif direction1 == 1:
                    y1 = y1 + 2 * r
                elif direction1 == 2:
                    x1 = x1 - 2 * r
                elif direction1 == 3:
                    y1 = y1 - 2 * r
                else:
                    x1 = x1 + 2 * r

                if i % 2 == 0:
                    color1 = YELLOW
                else:
                    color1 = ORANGE
                xy.append((x1, y1, color1))
                pygame.draw.circle(sc, color1, (int(x1), int(y1)), r)
                if proverka((x, y), (x1, y1)) and i > 1:
                    return 1
                if x + r >= WIN_WIDTH or y + r >= WIN_HEIGHT or x - r <= 0 or y - r <= 0:
                    return 1

            for i in range(len(enemies)):
                pygame.draw.circle(sc, RED, enemies[i], 15)
                pygame.draw.circle(sc, WHITE, (enemies[i][0] + 6, enemies[i][1] - 6), 5)
                pygame.draw.circle(sc, WHITE, (enemies[i][0] - 6, enemies[i][1] - 6), 5)
                pygame.draw.circle(sc, BLACK, (enemies[i][0] + 6, enemies[i][1] - 6), 3)
                pygame.draw.circle(sc, BLACK, (enemies[i][0] - 6, enemies[i][1] - 6), 3)
                pygame.draw.rect(sc, BLACK, (enemies[i][0] - 6, enemies[i][1] + 6, 15, 3))

            turns_copy = turns[:]
            x1 = x
            y1 = y
            direction1 = direction
            for i in range(l - 1):
                if turns_copy:
                    if direction1 == 1:
                        a = y1 + 2 * r
                        y2 = y1
                        y1 = turns_copy[-1][1]
                        if 2 * r <= abs(y1 - y2):
                            y1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 2:
                                x1 -= catet[int(abs(y1 - y2))]
                            else:
                                x1 += catet[int(abs(y1 - y2))]
                    elif direction1 == 2:
                        a = x1 - 2 * r
                        x2 = x1
                        x1 = turns_copy[-1][0]
                        if 2 * r <= abs(x1 - x2):
                            x1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 1:
                                y1 += catet[int(abs(x1 - x2))]
                            else:
                                y1 -= catet[int(abs(x1 - x2))]
                    elif direction1 == 3:
                        a = y1 - 2 * r
                        y2 = y1
                        y1 = turns_copy[-1][1]
                        if 2 * r <= abs(y1 - y2):
                            y1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 2:
                                x1 -= catet[int(abs(y1 - y2))]
                            else:
                                x1 += catet[int(abs(y1 - y2))]
                    else:
                        a = x1 + 2 * r
                        x2 = x1
                        x1 = turns_copy[-1][0]
                        if 2 * r <= abs(x1 - x2):
                            x1 = a
                        else:
                            direction1 = turns_copy[-1][2]
                            turns_copy.pop()
                            if direction1 == 1:
                                y1 += catet[int(abs(x1 - x2))]
                            else:
                                y1 -= catet[int(abs(x1 - x2))]
                elif direction1 == 1:
                    y1 = y1 + 2 * r
                elif direction1 == 2:
                    x1 = x1 - 2 * r
                elif direction1 == 3:
                    y1 = y1 - 2 * r
                else:
                    x1 = x1 + 2 * r

                if i % 2 == 0:
                    color1 = YELLOW
                else:
                    color1 = ORANGE
                xy.append((x1, y1, color1))
                pygame.draw.circle(sc, color1, (int(x1), int(y1)), r)

            text = f1.render(str(l - 5), 1, (0, 0, 0))
            sc.blit(text, (10, 50))
            pygame.display.update()


try:
    f2 = pygame.font.SysFont('calibri', 40)
    play()
    while True:
        sc.fill(WHITE)
        text1 = f2.render('Ты проиграл. Твой результат - ' + str(l - 5), 1, RED)
        sc.blit(text1, (WIN_WIDTH // 2 - 250, WIN_HEIGHT // 5))
        pygame.draw.circle(sc, RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2), 70)
        text2 = f2.render('Играть', 1, WHITE)
        sc.blit(text2, (WIN_WIDTH // 2 - 60, WIN_HEIGHT // 2 - 20))
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == QUIT:
                exit()
            if (i.type == MOUSEBUTTONDOWN and i.button == 1 and
                    proverka(i.pos, (WIN_WIDTH // 2, WIN_HEIGHT // 2), 0, 70)):
                play()
                continue
except Exception as e:
    print(e)
