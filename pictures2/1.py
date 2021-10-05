import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill('blue')

white = (0, 0, 0)
gray = (102, 99, 112)
black = (255, 255, 255)
yellow = (255, 221, 85)
yellow2 = (255, 230, 128)
blue = (71, 136, 147)
blue2 = (2, 57, 147)
blue3 = (5, 64, 85)

surface = pygame.Surface((600, 800), pygame.SRCALPHA)


def big_bird(x, y, scale, orientation):
    # Рисует большую птицу
    # x, y - позиция на экране
    # scale - масштаб
    # orientation - False если рисуем зеркальную птицу, True если обычную
    birds = pygame.Surface((600, 800), pygame.SRCALPHA)

    surface1 = pygame.Surface((300, 350), pygame.SRCALPHA)
    pygame.draw.polygon(surface1, black, ((113, 285), (136, 208), (226, 309), (156, 302)))
    pygame.draw.polygon(surface1, white, ((113, 285), (136, 208), (226, 309), (156, 302)), 1)
    birds.blit(surface1, (0, 15))

    surface1 = pygame.Surface((300, 400), pygame.SRCALPHA)
    pygame.draw.polygon(surface1, black, (
        (288, 216), (266, 168), (250, 147), (241, 135), (218, 131), (135, 132), (105, 129), (70, 121), (46, 112),
        (8, 91), (0, 90), (45, 157), (131, 172), (141, 181), (159, 201), (176, 218), (211, 239),))
    pygame.draw.polygon(surface1, white, (
        (288, 216), (266, 168), (250, 147), (241, 135), (218, 131), (135, 132), (105, 129), (70, 121), (46, 112),
        (8, 91), (0, 90), (45, 157), (131, 172), (141, 181), (159, 201), (176, 218), (211, 239),), 2)
    surface1 = pygame.transform.rotozoom(surface1, -15, 1)
    birds.blit(surface1, (50, 20))

    surface1 = pygame.Surface((300, 400), pygame.SRCALPHA)
    pygame.draw.polygon(surface1, black, (
        (288, 216), (266, 168), (250, 147), (241, 135), (218, 131), (135, 132), (105, 129), (70, 121), (46, 112),
        (8, 91), (0, 90), (45, 157), (131, 172), (141, 181), (159, 201), (176, 218), (211, 239)))
    pygame.draw.polygon(surface1, white, (
        (288, 216), (266, 168), (250, 147), (241, 135), (218, 131), (135, 132), (105, 129), (70, 121), (46, 112),
        (8, 91), (0, 90), (45, 157), (131, 172), (141, 181), (159, 201), (176, 218), (211, 239)), 2)
    birds.blit(surface1, (20, 75))

    surface1 = pygame.Surface((100, 30), pygame.SRCALPHA)
    pygame.draw.polygon(surface1, yellow, ((0, 15), (62, 22), (76, 5), (40, 10), (4, 0)))
    pygame.draw.polygon(surface1, white, ((0, 15), (62, 22), (76, 5), (40, 10), (4, 0)), 2)
    birds.blit(surface1, (500, 276))
    surface1 = pygame.transform.flip(surface1, False, True)
    birds.blit(surface1, (500, 266))

    surface1 = pygame.Surface((81, 63), pygame.SRCALPHA)
    pygame.draw.polygon(surface1, yellow2, (
        (8, 28), (12, 63), (19, 29), (27, 21), (35, 21), (76, 39), (56, 23), (42, 21), (53, 18), (81, 29), (60, 15),
        (42, 14), (52, 11), (69, 11), (78, 16), (74, 8), (63, 2), (47, 2), (24, 12)))
    pygame.draw.polygon(surface1, white, (
        (8, 28), (12, 63), (19, 29), (27, 21), (35, 21), (76, 39), (56, 23), (42, 21), (53, 18), (81, 29), (60, 15),
        (42, 14), (52, 11), (69, 11), (78, 16), (74, 8), (63, 2), (47, 2), (24, 12)), 1)
    birds.blit(surface1, (440, 430))
    birds.blit(surface1, (415, 455))

    surface3 = pygame.Surface((600, 500), pygame.SRCALPHA)
    surface2 = pygame.Surface((140, 150), pygame.SRCALPHA)
    pygame.draw.ellipse(surface2, black, (10, 30, 110, 30))
    pygame.draw.ellipse(surface2, black, (30, 0, 110, 30))
    surface2 = pygame.transform.rotozoom(surface2, -15, 1)
    surface3.blit(surface2, (300, 373))
    surface1 = pygame.Surface((100, 150), pygame.SRCALPHA)
    pygame.draw.ellipse(surface1, black, (0, 5, 40, 120))
    pygame.draw.ellipse(surface1, black, (30, 0, 40, 120))
    surface1 = pygame.transform.rotozoom(surface1, 30, 1)
    surface3.blit(surface1, (260, 270))
    pygame.draw.ellipse(surface3, black, (200, 240, 205, 95))
    pygame.draw.ellipse(surface3, black, (362, 256, 104, 46))
    pygame.draw.ellipse(surface3, black, (440, 243, 75, 46))
    pygame.draw.ellipse(surface3, white, (484, 255, 15, 12))
    birds.blit(surface3, (0, 20))

    birds2 = pygame.Surface((560, 400), pygame.SRCALPHA)
    birds2.blit(birds, (0, 0), (20, 110, 560, 400))
    birds2 = pygame.transform.rotozoom(birds2, 0, scale)
    birds2 = pygame.transform.flip(birds2, not orientation, False)

    surface.blit(birds2, (x, y))


def fish(x, y, angle, scale, orientation):
    # Рисует рыбу
    # x, y - позиция на экране
    # angle - угол поворота
    # scale - масштаб
    # orientation - False если рисуем зеркальную рыбу, True если обычную
    surface1 = pygame.Surface((220, 115), pygame.SRCALPHA)
    pygame.draw.polygon(surface1, gray, ((160, 60), (171, 58), (196, 73), (168, 88)))
    pygame.draw.arc(surface1, blue, (65, 33, 148, 50), 0.4, 2.74, 30)
    pygame.draw.arc(surface1, blue, (65, 13, 148, 50), 3.44, 6, 30)
    pygame.draw.polygon(surface1, blue, ((67, 45), (14, 80), (4, 35)))
    pygame.draw.polygon(surface1, gray, ((135, 33), (94, 0), (164, 15), (172, 24), (171, 35)))
    pygame.draw.polygon(surface1, gray, ((97, 59), (80, 79), (112, 84), (114, 62)))
    pygame.draw.circle(surface1, blue2, (170, 47), 7)
    pygame.draw.circle(surface1, blue3, (170, 47), 5)
    surface1 = pygame.transform.rotozoom(surface1, angle, scale)
    surface1 = pygame.transform.flip(surface1, not orientation, False)
    surface.blit(surface1, (x, y))


def bird(x, y, angle, scale):
    # Рисует маленьку птицу
    # x, y - позиция на экране
    # angle - угол поворота
    # scale - масштаб
    surface1 = pygame.Surface((200, 100), pygame.SRCALPHA)
    pygame.draw.arc(surface1, black, (0, 0, 100, 50), 0.1, 3.04, 3)
    pygame.draw.arc(surface1, black, (100, 0, 100, 50), 0.1, 3.04, 3)
    surface1 = pygame.transform.rotozoom(surface1, angle, scale)
    surface.blit(surface1, (x, y))


for i in range(0, 410, 1):
    pygame.draw.rect(screen, (round(33+i*0.5), round(33+i*0.28), round(220 - ((i-205)**2)/350)), (0, i, 600, 1))
    pygame.draw.rect(screen, (round(0), round(100-i*0.2), round(160-i*0.3)), (0, i+410, 600, 1))


big_bird(400, 370, 0.30, True)
big_bird(0, 450, 0.60, True)
big_bird(200, 350, 0.20, False)
fish(400, 600, 0, 0.6, True)
fish(280, 470, 0, 0.7, False)
fish(20, 650, 0, 0.7, True)
bird(60, 0, 20, 0.9)
bird(300, 130, 0, 0.9)
bird(100, 220, -20, 0.9)
bird(520, 250, 0, 0.4)
bird(500, 290, 0, 0.4)
bird(500, 180, 0, 0.4)
bird(300, 230, 10, 0.4)
bird(275, 200, 10, 0.4)
bird(200, 170, 10, 0.4)
bird(300, 90, -10, 0.4)
bird(330, 30, -10, 0.4)

screen.blit(surface, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
