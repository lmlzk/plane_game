import pygame
from random import *


class Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100


class Bullet_Supply(Supply):
    def __init__(self, bg_size):
        image = "images/bullet_supply.png"
        super().__init__(bg_size,  image)


class Bomb_Supply(Supply):
    def __init__(self, bg_size):
        image = "images/bomb_supply.png"
        super().__init__(bg_size, image)

