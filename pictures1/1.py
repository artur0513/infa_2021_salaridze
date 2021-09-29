#Exercise 1 - smile

import pygame

pygame.init()

FPS = 30
x = 400
y = 400
screen = pygame.display.set_mode((x, y))

yellow = (255, 225, 0)
gray = (224, 255, 255)
black = (20, 20, 20)
red = (200, 10, 30)

pygame.draw.rect(screen, gray, (0, 0, x, y))
pygame.draw.circle(screen, yellow, (200, 200), 100)
pygame.draw.circle(screen, black, (200, 200), 100, 3)

pygame.draw.circle(screen, red, (150, 175), 20)
pygame.draw.circle(screen, black, (150, 175), 20, 1)
pygame.draw.circle(screen, black, (150, 175), 8)

pygame.draw.circle(screen, red, (250, 175), 16)
pygame.draw.circle(screen, black, (250, 175), 16, 1)
pygame.draw.circle(screen, black, (250, 175), 8)

pygame.draw.polygon(screen, black, [[180, 180], [120, 130], [130, 120], [190, 160]])

pygame.draw.polygon(screen, black, [[220, 170], [270, 150], [260, 140], [220, 160]])

pygame.draw.polygon(screen, black, [[150, 240], [240, 240], [240, 260], [150, 260]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)

pygame.quit()