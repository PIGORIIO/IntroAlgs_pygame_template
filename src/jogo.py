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
rows = 4
cols = 5
alien_direction = 1
alien_cooldown = 1000#bullet cooldown in milliseconds
last_alien_shot = pygame.time.get_ticks()

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
        # Set Movement Speed
        speed = 8
        # Set a cooldown variable
        cooldown = 600 #milliseconds

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed

        # Record Current Time
        time_now = pygame.time.get_ticks()

        # Shoot
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now

        # Update Mask
        self.mask = pygame.mask.from_surface(self.image)

        # Draw Health Bar
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
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()



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
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)


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


# Create Aliens Bullets Class
class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/imagens/star_tiny.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(
            self,
            spaceship_group,
            False,
            pygame.sprite.collide_mask
        ):
            self.kill()

            # Reduce Spaceship Health
            spaceship.health_remaining -= 1

            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)


# Create Explosion Class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 4):
            img = pygame.image.load(f"assets/imagens/exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (160, 160))

            # Add the image to the list
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 3

        #update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # If the animation is complete, delete explosion
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


# Create sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()


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

    # Create Random Alien Bullets
    # Record Current Time
    time_now = pygame.time.get_ticks()

    # Shoot
    if (
        time_now - last_alien_shot > alien_cooldown
        and len(alien_bullet_group) < 5
        and len(alien_group) > 0
    ):
        attacking_alien = random.choice(alien_group.sprites())
        alien_bullet = Alien_Bullets(
            attacking_alien.rect.centerx,
            attacking_alien.rect.bottom
        )
        alien_bullet_group.add(alien_bullet)
        last_alien_shot = time_now

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # UPDATE
    spaceship_group.update()
    bullet_group.update()
    alien_bullet_group.update()
    explosion_group.update()

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
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)

    pygame.display.update()

pygame.quit()