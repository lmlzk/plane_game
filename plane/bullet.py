import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, image, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet1(Bullet):
    def __init__(self, position):
        image = "images/bullet.png"
        speed = 12
        super().__init__(position, image, speed)


class Bullet2(Bullet):
    def __init__(self, position):
        image = "images/bullet2.png"
        speed = 14
        super().__init__(position, image, speed)


class Bullet3(Bullet):
    def __init__(self, position):
        image = "images/bullet1.png"
        speed = 12
        super().__init__(position, image, speed)
        self.speed2 = 5

    def move(self):
        super().move()
        self.rect.left -= self.speed2
        if self.rect.left < 0:
            self.active = False


class Bullet4(Bullet):
    def __init__(self, position, bg_size):
        image = "images/bullet1.png"
        speed = 12
        super().__init__(position, image, speed)
        self.speed2 = 5
        self.width = bg_size[0]

    def move(self):
        super().move()
        self.rect.left += self.speed2
        if self.rect.left > self.width:
            self.active = False


class Bullet5(Bullet):
    def __init__(self, position):
        image = "images/bullet1.png"
        speed = 12
        super().__init__(position, image, speed)

