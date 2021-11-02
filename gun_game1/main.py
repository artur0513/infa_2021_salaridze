import math
import random

import pygame

pygame.font.init()
font = pygame.font.Font(None, 30)

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (20, 20, 20)
WHITE = 0xFFFFFF
GREY = (150, 150, 150)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
TANKGREEN = (100, 120, 70)

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)

#Рисуем поверхность с танком
tanksurf = pygame.Surface((300, 300))
tanksurf.set_colorkey((0, 0, 0))
pygame.draw.circle(tanksurf, GREY, (50, 250), 40)
pygame.draw.circle(tanksurf, GREY, (250, 250), 40)
pygame.draw.rect(tanksurf, GREY, (50, 210, 200, 80))
pygame.draw.circle(tanksurf, BLACK, (50, 250), 30)
pygame.draw.circle(tanksurf, BLACK, (250, 250), 30)
pygame.draw.circle(tanksurf, BLACK, (100, 250), 30)
pygame.draw.circle(tanksurf, BLACK, (150, 250), 30)
pygame.draw.circle(tanksurf, BLACK, (200, 250), 30)
pygame.draw.polygon(tanksurf, TANKGREEN, ((0, 230), (60, 170), (60, 230)))
pygame.draw.polygon(tanksurf, TANKGREEN, ((300, 230), (240, 170), (240, 230)))
pygame.draw.rect(tanksurf, TANKGREEN, (60, 170, 180, 60))
pygame.draw.circle(tanksurf, TANKGREEN, (150, 170), 60)

#Размещаем поверхность с танком на заданной поверхности, в координатах x, y и с масштабом scale
def draw_tank(surface, x , y, scale=1):
    if scale != 1:
        tanksurf_tranformed = pygame.transform.scale(tanksurf, (round(300*scale), round(300*scale)))
        surface.blit(tanksurf_tranformed, (x, y))
    else:
        surface.blit(tanksurf, (x, y))

#Класс отвечающий за кнопки
class Button:
    def __init__(self, surface, x, y, width, height, buttontext):
        """
        :param surface: Поверхность для отрисовки кнопки
        :param x: Координата x левого верхнего угла кнопки
        :param y: Координата y левого верхнего угла кнопки
        :param width: Ширина кнопки
        :param height: Высота кнопки
        :param buttontext: Текст на кнопке
        """
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #Рисуем поверхность с черной кнопкой
        self.buttonsurf = pygame.Surface((self.width, self.height))
        self.buttonsurf.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.buttonsurf, BLACK, (0, 0, self.width, self.height), 7)
        text = font.render(buttontext, True, (10, 10, 10))
        self.buttonsurf.blit(text, ((self.width - text.get_width())/2, (self.height - text.get_height())/2))

        #Рисуем поверхность с серой кнопкой, нужна для создания ээфекта обьема и анимации нажатия
        self.buttonshadow = pygame.Surface((self.width, self.height))
        self.buttonshadow.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.buttonshadow, GREY, (0, 0, self.width, self.height), 7)
        text = font.render(buttontext, False, (150, 150, 150))
        self.buttonshadow.blit(text, ((self.width - text.get_width()) / 2, (self.height - text.get_height()) / 2))

        self.pressed = False
        self.nexttick = False

    def draw(self):
        # Рисуем кнопку по разному в зависимости от того нажата ли она
        if self.pressed and self.nexttick:
            self.pressed = False
            self.nexttick = False

        if not self.pressed:
            self.surface.blit(self.buttonshadow, (self.x + 3, self.y + 3))
            self.surface.blit(self.buttonsurf, (self.x, self.y))
        else:
            self.surface.blit(self.buttonshadow, (self.x + 3, self.y + 3))
            self.surface.blit(self.buttonsurf, (self.x + 2, self.y + 2))

    def check(self, event):
        #Проверка на нажатие кнопки
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x < event.pos[0] < self.x + self.width:
                if self.y < event.pos[1] < self.y + self.height:
                    self.pressed = True
                    return True
        if event.type == pygame.MOUSEBUTTONUP and self.pressed == True:
            self.nexttick = True
        return False

#Класс для эффектов выхлопных газов от танка (создает летающие шарики серого цвета)
class Particle:
    def __init__(self, x, y, alpha, r, screen):
        """
        :param x: Координата x центра кружка
        :param y: Координата y центра кружка
        :param alpha: Начальная прозрачность кружка
        :param r: Начальный радиус кружука
        :param screen: Поверхность для отрисовки
        """
        self.x = x
        self.y = y
        self.r = r
        self.vy = 0
        self.vx = random.randint(-3, 3)
        self.velocity = 1
        self.alpha = alpha
        self.screen = screen
    def update(self):
        #Обновляем позицию на экране, скорость, прозрачность шарика
        self.vy += self.velocity
        self.y -= self.vy
        self.x += self.vx
        self.r += 2
        self.alpha -= 2
        self.partsurface = pygame.Surface((self.r*2, self.r*2))
        pygame.draw.circle(self.partsurface, GREY, (self.r, self.r), self.r)
        self.partsurface.set_colorkey((0,0,0))
        self.partsurface.set_alpha(self.alpha)
        self.screen.blit(self.partsurface, (self.x - self.r, self.y - self.r))


class Ball:
    def __init__(self, _screen, x=40, y=450):
        """
        :param _screen: Поверхность для отрисовки
        :param x: Начальная координата x
        :param y: Начальная координата y
        """
        self.screen = _screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)
        self.live = 30
        self.alpha = 255

        self.max_c = 6
        self.c = 0

    def update(self):
        """Переместить мяч по прошествии единицы времени. И обработать столкновение со стенками.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy

        if self.x > WIDTH - self.r and self.vx > 0:
            self.vx *= -0.6
            self.vy *= 0.8
            self.x = WIDTH - self.r
            self.c += 1
        if self.y > HEIGHT - self.r and self.vy < 0:
            self.vy *= -0.6
            self.vx *= 0.8
            self.y = HEIGHT - self.r
            self.c += 1
        if self.c > self.max_c:
            if self.alpha > 0:
                self.alpha -= 4
            else:
                self.alpha = 0
        self.vy -= 1

    def draw(self):
        # Отрисовать шарик с учетом его прозрачности(После нескольких столкновений шарик плавно становится прозрачным и исчезает)
        self.surface1 = pygame.Surface((self.r*2, self.r*2))
        self.surface1.set_alpha(self.alpha)
        pygame.draw.circle(self.surface1, self.color, (self.r, self.r), self.r)
        self.surface1.set_colorkey((0, 0, 0))
        screen.blit(self.surface1, (self.x - self.r, self.y - self.r))

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
            Если проверяем столкновение двух обьектов класса Ball, то меняем им скорости после столкновения.
        """
        dist = (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 - (self.r + obj.r) ** 2
        if dist > 0:
            return False
        else:
            if type(obj) == Ball:
                p1 = complex(self.x, self.y)
                p2 = complex(obj.x, obj.y)
                v1 = complex(self.vx, self.vy)
                v2 = complex(obj.vx, obj.vy)
                p12 = p1 - p2
                d = ((v1 - v2) / p12).real * p12
                self.vx = (v1 - d).real
                self.vy = (v1 - d).imag
                obj.vx = (v2 + d).real
                obj.vy = (v2 + d).imag
            else:
                self.alpha = 0
            return True


#Класс отвечающий за пушку и ее перемещение
class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

        self.timer = 0

        self.x = 100
        self.y = 540

        self.mousex = 100
        self.mousey = 100

        self.vx = 0
        self.maxspeed = 3
        self.velocity = 0

        self.moving_right = False
        self.moving_left = False

        self.reloadtime = self.defreloadtime = 90
        self.bulletsleft = self.defbulletsleft = 8

        self.fuel = 3000
        self.fuellinecolor = GREEN

    def fire2_start(self, event):
        #Начать увеличивать мощность пушки (зажать ЛКМ)
        if self.bulletsleft > 0:
            self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        if self.bulletsleft > 0:
            bullet += 1
            new_ball = Ball(self.screen, self.x, self.y)
            new_ball.r += 5
            self.an2 = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an2)
            new_ball.vy = - self.f2_power * math.sin(self.an2)
            balls.append(new_ball)
            self.f2_on = 0
            self.f2_power = 10
            self.bulletsleft -= 1

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event.type == pygame.MOUSEMOTION:
            self.mousex = event.pos[0]
            self.mousey = event.pos[1]
        self.an = - math.atan2((self.mousey-self.y), (self.mousex-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def update(self):
        """
        Обработка всех остальных событий связанных с танком
        Отрисовка пушки с заданным углом и размером.
        Перезарядка пушки и отрисовка количества оставшихся патронов и таймера перезарядки.
        Создание эффектов выхлопных газов.
        Обновление и отрисовка количества оставшегося топлива.
        Перемещение танка на экране
        """
        self.timer = (self.timer + 1)%1000
        if self.an < 0 and self.an > -math.pi/2:
            self.an = 0
        if self.an < 0 and self.an < -math.pi/2:
            self.an = math.pi
        self.sin = math.sin(self.an)
        self.cos = math.cos(self.an)
        self.gunxcoord = self.x + (30 + self.f2_power)*self.cos
        self.gunycoord = self.y - (30 + self.f2_power)*self.sin
        pygame.draw.polygon(self.screen, BLACK, ((self.x - 5*self.sin, self.y-5*self.cos), (self.x + 5*self.sin, self.y + 5*self.cos),
                                                 (self.gunxcoord + 5*self.sin, self.gunycoord + 5*self.cos),
                                                 (self.gunxcoord - 5*self.sin, self.gunycoord - 5*self.cos)))

        draw_tank(self.screen, self.x - 75, self.y - 85, 0.5)

        if self.bulletsleft == 0 and self.reloadtime > 0:
            self.reloadtime -= 1
            text = font.render("Reloading: ", True, (0, 0, 0))
            self.screen.blit(text, (50, 50))
            pygame.draw.line(self.screen, RED, (50 + text.get_width(), 50 + text.get_height()/2), (50 + text.get_width() + self.reloadtime, 50 + text.get_height()/2), 10)
        if self.reloadtime == 0:
            self.reloadtime = self.defreloadtime
            self.bulletsleft = self.defbulletsleft

        text = font.render("Bullets left: " + str(round(self.bulletsleft)), True, (0, 0, 0))
        self.screen.blit(text, (50, 30))

        text = font.render("Fuel left: ", True, (0, 0, 0))
        self.screen.blit(text, (50 ,10))
        if self.fuel > 0:
            pygame.draw.line(self.screen, self.fuellinecolor, (50 + text.get_width(), text.get_height()/2 + 10), (50 + text.get_width() + self.fuel/33.3, text.get_height()/2 + 10), 10)


        if self.fuel > 0:
            if self.moving_left:
                self.vx = -self.maxspeed

            if self.moving_right:
                self.vx = self.maxspeed

            if (self.moving_left or self.moving_right) and self.timer % 2 == 0:
                new_particle = Particle(self.x - 60, self.y + 8, 40, 4, self.screen)
                particles.append(new_particle)
                self.fuel -= 5

            elif self.timer % 5 == 0:
                new_particle = Particle(self.x - 60, self.y + 8, 40, 2, self.screen)
                particles.append(new_particle)
                self.fuel -= 2

            self.x += self.vx
            if abs(self.vx) > 1:
                self.fuellinecolor = RED
                self.vx -= 0.5 * self.vx / abs(self.vx)
            else:
                self.fuellinecolor = GREEN
                self.vx = 0
        else:
            self.fuel = 0



    def move(self, event):
        """
        Управление танком с клавиатуры, перемещение вправо, влево, перезарядка
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.moving_left = True
            if event.key == pygame.K_d:
                self.moving_right = True
            if event.key == pygame.K_r and self.bulletsleft != self.defbulletsleft:
                self.bulletsleft = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.moving_left = False
            if event.key == pygame.K_d:
                self.moving_right = False


    def power_up(self):
        # Увеличение мощности пушки при зажатой ЛКМ.
        if self.f2_on:
            if self.f2_power < 50:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

# Класс для мишеней
class Target:
    def __init__(self, _screen, _movingtype = 0):
        """
        :param _screen: Поверхность для отрисовки
        :param _movingtype: Тип движения мишени, 0  если не движется, 1 если движется вправо влево, 2 вверх вниз
        """
        self.screen = _screen
        self.movingtype = _movingtype

        self.live = True
        self.defcooldown = self.cooldown = 90

        x = self.x = random.randint(500, 780)
        y = self.y = random.randint(200, 550)
        r = self.r = random.randint(10, 30)
        color = self.color = RED
        self.reward = 60 - self.r

        if self.movingtype == 1:
            self.startpoint = self.x
            self.endpoint = self.x + random.randint(-200, -50)
            self.speed = random.randint(1, 4)

        if self.movingtype == 2:
            self.startpoint = self.y
            self.endpoint = self.y + random.randint(-200, -50)
            self.speed = random.randint(1, 4)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = random.randint(500, 780)
        y = self.y = random.randint(200, 550)
        r = self.r = random.randint(10, 30)
        color = self.color = RED
        self.reward = 60 - self.r

        if self.movingtype == 1:
            self.startpoint = self.x
            self.endpoint = self.x + random.randint(-200, -50)
            self.speed = random.randint(1, 4)

        if self.movingtype == 2:
            self.startpoint = self.y
            self.endpoint = self.y + random.randint(-200, -50)
            self.speed = random.randint(1, 4)

    def hit(self):
        """Попадание шарика в цель. Возвращает количество очков при попадании"""
        if self.live:
            self.new_target()
            self.live = False
            return self.reward
        else:
            return 0

    def draw(self):
        # Отрисовка мишени
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def update(self):
        # Обновленеие мишени (таймер до возродения и движение мишени)
        if not self.live:
            if self.cooldown > 0:
                self.cooldown -= 1
            else:
                self.cooldown = self.defcooldown
                self.live = True
        else:
            self.draw()
        if self.movingtype == 1:
            self.x += self.speed
            if self.x < self.endpoint or self.x > self.startpoint:
                self.speed *= -1

        if self.movingtype == 2:
            self.y += self.speed
            if self.y < self.endpoint or self.y > self.startpoint:
                self.speed *= -1

points = 0
bullet = 0
balls = []
particles = []
clock = pygame.time.Clock()
gun = Gun(screen)
targets = [Target(screen, i%3) for i in range(6)]
resetbutton = Button(screen, 500, 10, 100, 50, 'reset')

# Сброс игры до начального положения
def new_game():
    global points
    global bullet
    global balls
    global particles
    global clock
    global gun
    global targets
    points = 0
    bullet = 0
    balls = []
    particles = []
    clock = pygame.time.Clock()
    gun = Gun(screen)
    targets = [Target(screen, i % 3) for i in range(6)]

finished = False
while not finished:
    clock.tick(FPS)
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT))
    gun.update()
    resetbutton.draw()
    for p in particles:
        p.update()
        if p.alpha < 0:
            particles.remove(p)
    for t in targets:
        t.update()
    for b in balls:
        b.update()
        for t in targets:
            if b.hittest(t):
                points += t.hit()
        for b2 in balls:
            if b2 != b:
                b.hittest(b2)
        if b.alpha == 0:
            balls.remove(b)
        b.draw()
    text = font.render("Score: " + str(round(points)), True, (0, 0, 0))
    screen.blit(text, (WIDTH - 150, 30))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif resetbutton.check(event):
            new_game()
        elif not resetbutton.pressed:
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                gun.fire2_end(event)
            gun.targetting(event)
            gun.move(event)

    gun.power_up()

pygame.quit()
