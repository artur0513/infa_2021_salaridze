import math
import random

import pygame

pygame.init()

pygame.font.init()
font = pygame.font.Font(None, 25)  # Шрифт для надписей

file = open('result.txt', 'a')  # Файл для записей результатов

FPS = 30

score = 0  # Количество очков у игрока
timer = 600  # Время, оставшееся до конца игры, выраженное в проходах цикла (Время в секунах = timer/fps)

xscreen = 600
yscreen = 600  # Параметры окна
delta = 30  # Отступ от рамок окна, чтобы шарики не слишком заползали за рамки

ballminsize = 25
ballmaxsize = 50  # Минимальный и максимальный размер появляющихся шариков

ballminspeed = 10
ballmaxspeed = 30  # Минимальная и максимальная скорость появляющихся шариков

screen = pygame.display.set_mode((xscreen, yscreen))  # Создание окна


def randcolor():  # Функция для генерации случайных цветов для шариков
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def generatepoints(number):  # Функция генерирует стратовые координаты шариков так, чтобы они не лежали слишком близко
    points = []
    for i in range(number):
        x = i * yscreen / number + random.randint(delta, yscreen / number - delta)
        y = random.randint(delta + xscreen * (i % 2) / 2, (xscreen - delta) / 2 + xscreen * (i % 2) / 2)
        points.append([x, y])
    return (points)


class Ball:  # Класс для шариков

    def __init__(self, _ballsurface, _restartimer=100, _gravity=False, coords=[0, 0]):  # Инициализация обьекта класса
        # _ballsurface - поверхность, на которой рисуем шарик _moving - движется ли шарик
        # _restartimer - время,
        # через которое шарик снова появится на экране, после того как на него кликнули (время возрождения)
        # _gravity - подвержен ли шарик гравитации, работает только если _moving = true
        if coords == [0, 0]:
            self.x = random.randint(0 + delta, xscreen - delta)
            self.y = random.randint(0 + delta, yscreen - delta)  # Генерируем случайное положение шарика на экране
        else:
            self.x = coords[0]
            self.y = coords[1]
        self.r = random.randint(ballminsize, ballmaxsize)  # Генерируем случайный размер шарика
        self.active = True  # Шарик активен, то есть двигается по экрану и на него можно кликнуть
        self.ballsurface = _ballsurface

        self.gravity = _gravity

        self.pointtimer = 20  # Время на которое появляется надпись с полученным количеством очков
        self.defaulttimer = _restartimer  # Время возрождения по умолчанию
        self.timer = self.defaulttimer  # Время возрождения, которое будет уменьшаться
        self.color = randcolor()  # Установили цвет шарику
        self.speedx = random.randint(ballminspeed, ballmaxspeed) / 5  # Если шарик движущийся,
        self.speedy = random.randint(ballminspeed, 1.5 * ballmaxspeed) / 5  # то генерируем скорость
        self.reward = (ballmaxsize - self.r) + self.speedy + self.speedx + 10  # Считаем награду
        if self.gravity:
            self.reward = (ballmaxsize - self.r) + self.speedy + self.speedx + 25  # Если шарик с гравитцией,
            # то награда больше

    def changeball(self):  # Функция, соданная чтобы менять параметры шарика перед его слудующим "возрождением"
        # Эта функция во многом аналогична функции инициализации
        self.r = random.randint(ballminsize, ballmaxsize)
        self.color = randcolor()
        self.speedx = random.randint(ballminspeed, ballmaxspeed) / 5
        self.speedy = random.randint(ballminspeed, 1.5 * ballmaxspeed) / 5
        self.reward = (ballmaxsize - self.r) + self.speedy + self.speedx + 10
        if self.gravity:
            self.reward = (ballmaxsize - self.r) + self.speedy + self.speedx + 25

    def distance(self, mousex, mousey):  # Определяем, кликнули ли мы по шарику или мимо
        dist = (mousex - self.x) ** 2 + (mousey - self.y) ** 2 - self.r ** 2  # Расстояние до клика минус радиус шара
        if dist < 0 and self.active:  # Если кликунли по шарику
            self.active = False  # То шарик на время становится неактивным
            self.lastdeathx = self.x
            self.lastdeathy = self.y  # Запоминаем координаты "смерти" шарика
            return self.reward  # Возвращаем награду
        return 0  # Если кликнули мимо, то возвращаемая награда 0

    def collisioncheck(self, obj):
        distance = (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 - (self.r + obj.r) ** 2
        if distance < 0:
            p1 = complex(self.x, self.y)
            p2 = complex(obj.x, obj.y)
            v1 = complex(self.speedx, self.speedy)
            v2 = complex(obj.speedx, obj.speedy)
            p12 = p1 - p2
            d = ((v1 - v2) / p12).real * p12
            if self.active and obj.active:
                self.speedx = (v1 - d).real
                self.speedy = (v1 - d).imag
                obj.speedx = (v2 + d).real
                obj.speedy = (v2 + d).imag
            if not self.active and not obj.active:
                self.speedx = (v1 - d).real
                self.speedy = (v1 - d).imag
                obj.speedx = (v2 + d).real
                obj.speedy = (v2 + d).imag
            if not self.active and obj.active:
                self.speedx = (v1 - d).real
                self.speedy = (v1 - d).imag
            if self.active and not obj.active:
                obj.speedx = (v2 + d).real
                obj.speedy = (v2 + d).imag

    def update(self):  # Функция обновления шарика, где мы считаем его новые координаты и прочее
        if self.active:  # Если шарик активен
            pygame.draw.circle(self.ballsurface, self.color, (self.x, self.y), self.r)  # Рисуем шарик
        self.x += self.speedx
        self.y += self.speedy
        if self.x > xscreen - delta and self.speedx > 0:  # Если выходим за пределы окна, то меняем скорость
            self.speedx *= -1
        if self.x < 0 + delta and self.speedx < 0:  # При этом проверяем куда направлена скорость, иначе
            self.speedx *= -1  # Шарики иногда "застревают" у края
        if self.y > yscreen - delta and self.speedy > 0:
            self.speedy *= -1
        if self.y < 0 + delta and self.speedy < 0:
            self.speedy *= -1
        if self.gravity:
            self.speedy += 0.3  # Если шарик с гравитацией, то меняем скорость
        if not self.active:  # Если шарик неактивен
            self.timer -= 1  # Мотаем таймер до возраждения
            if self.pointtimer > 0:  # Если таймер для показа очков еще не кончился
                points = font.render("+" + str(round(self.reward)), True, (255, 255, 255))  # Рисуем надпись с очками
                points.set_alpha(self.pointtimer * 25)  # Постепенно делаем надпись прозрачнее
                screen.blit(points, (self.lastdeathx + 10, self.lastdeathy + 10))
                self.surface1 = pygame.Surface((2 * self.r, 2 * self.r), pygame.SRCALPHA)
                self.surface1.set_alpha(self.pointtimer * 7)
                pygame.draw.circle(self.surface1, self.color, (self.r, self.r), self.r)
                screen.blit(self.surface1, (self.x - self.r, self.y - self.r))
                self.r += 1
                self.pointtimer -= 1  # Уменьшаем таймер показа написи с очками
                self.lastdeathy -= 1  # Постепенно перемещаем надпись с очками вверх

            if self.timer < 0:  # Если таймер до возраждения закончился
                self.pointtimer = 20
                self.timer = self.defaulttimer
                self.active = True  # То снова делаем шарик активным
                self.changeball()  # И меняем ему размеры, цвет и скорость


clock = pygame.time.Clock()
numberofballs = 10
coords = generatepoints(numberofballs)

balls = [Ball(screen, 100, i % 2, coords[i]) for i in range(numberofballs)]  # Создаем массив обьектов класса шар

result = False

nameentered = False  # Ввел ли игрок имя
name = ""  # Переменная для введенного имени

finished = False
while not finished:
    clock.tick(FPS)

    pygame.display.update()
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, xscreen, yscreen))  # Закрасили экран черным

    if not nameentered:  # Часть кода, отвечающая за введение имени игроком
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[0:-1]
                elif event.key == pygame.K_RETURN:
                    nameentered = True
                else:
                    name += event.unicode
        text4 = font.render("Write your name, than press enter:", True, (255, 255, 255))
        screen.blit(text4, (100, 80))
        text3 = font.render(name, True, (255, 255, 255))
        screen.blit(text3, (100, 100))

    if timer > 0 and nameentered:  # Основная часть игры
        timer -= 1
        text = font.render("Score: " + str(round(score)), True, (255, 255, 255))
        text2 = font.render("Time left: " + str(round(timer / FPS)), True, (255, 255, 255))
        screen.blit(text, (xscreen / 2 - 50, 20))
        screen.blit(text2, (xscreen / 2 - 50, 40))
        for i in balls:
            for j in balls:
                if i != j:
                    i.collisioncheck(j)
            i.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in balls:
                        score += i.distance(event.pos[0], event.pos[1])

    elif timer < 1:  # Таймер игры закончился, ввыводим результаты и записываем их в файл
        text = font.render("Game over", True, (255, 255, 255))
        screen.blit(text, (xscreen / 2 - 50, yscreen / 3))

        text = font.render("Score: " + str(round(score)), True, (255, 255, 255))
        screen.blit(text, (xscreen / 2 - 50, yscreen / 2))

        if not result:
            file.write(name + " " + str(round(score)) + '\n')
            file.close()
            result = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
pygame.quit()
