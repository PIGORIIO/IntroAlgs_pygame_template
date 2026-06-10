import pygame
from pygame.locals import *
import random

# Inicializa o Pygame
pygame.init()

# Define FPS
clock = pygame.time.Clock()
fps = 60

screen_width = 700
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Intergalactic Race - Um conflito além do terrestre')

# Define Game Variables
rows = 5
cols = 5
alien_direction = 1

# Define Colours
red = (255, 0, 0)
green = (0, 255, 0)

# load image
bg = pygame.image.load("assets/imagens/Space_Pixel2.png")


def draw_bg():
    screen.blit(bg, (0, 0))


# Create Spaceship Class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/imagens/Ship_1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        speed = 8
        cooldown = 600

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed

        time_now = pygame.time.get_ticks()

        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now

        pygame.draw.rect(
            screen,
            red,
            (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15)
        )

        if self.health_remaining > 0:
            pygame.draw.rect(
                screen,
                green,
                (
                    self.rect.x,
                    (self.rect.bottom + 10),
                    int(self.rect.width * (self.health_remaining / self.health_start)),
                    15
                )
            )


# Create Bullets Class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/imagens/star_small.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()


# Create Aliens Class
class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(
            "assets/imagens/Aliens" + str(random.randint(1, 5)) + ".png"
        )

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        pass


# Create sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()


def create_aliens():
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 100, 40 + row * 70)
            alien_group.add(alien)


create_aliens()

# Create Player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3)
spaceship_group.add(spaceship)

run = True
while run:

    clock.tick(fps)

    # Draw Background
    draw_bg()

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # UPDATE
    spaceship_group.update()
    bullet_group.update()

    # ALIEN MOVEMENT (CORRIGIDO E DENTRO DO LOOP)
    move_down = False

    for alien in alien_group:
        if alien.rect.right >= screen_width and alien_direction == 1:
            alien_direction = -1
            move_down = True
            break

        if alien.rect.left <= 0 and alien_direction == -1:
            alien_direction = 1
            move_down = True
            break

    for alien in alien_group:
        alien.rect.x += alien_direction * 2

        if move_down:
            alien.rect.y += 20

    # DRAW
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)

    pygame.display.update()

pygame.quit()