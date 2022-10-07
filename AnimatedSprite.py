import pygame
vec = pygame.math.Vector2
PLAYER_GRAVITY = 0.8
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
class AnimatedSprite(pygame.sprite.Sprite):
 
    def __init__(self, position):
        super(AnimatedSprite, self).__init__()
 
        size = (145, 120)
        images = []
        images.append(pygame.image.load('santasprites/png/Run (1).png'))
        images.append(pygame.image.load('santasprites/png/Run (2).png'))
        images.append(pygame.image.load('santasprites/png/Run (3).png'))
        images.append(pygame.image.load('santasprites/png/Run (4).png'))
        images.append(pygame.image.load('santasprites/png/Run (5).png'))
        images.append(pygame.image.load('santasprites/png/Run (6).png'))
        images.append(pygame.image.load('santasprites/png/Run (7).png'))
        images.append(pygame.image.load('santasprites/png/Run (8).png'))
        images.append(pygame.image.load('santasprites/png/Run (9).png'))
        images.append(pygame.image.load('santasprites/png/Run (10).png'))
        images.append(pygame.image.load('santasprites/png/Run (11).png'))
        jumpimages = []
        jumpimages.append(pygame.image.load('santasprites/png/Jump (1).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (2).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (3).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (4).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (5).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (6).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (7).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (8).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (9).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (10).png'))
        jumpimages.append(pygame.image.load('santasprites/png/Jump (11).png'))
 
        self.rect = pygame.Rect(position, size)
        self.isJump = False
        self.jumpCount = 10

        self.images = [pygame.transform.scale(image, size) for image in images]
        self.jumpimages = [pygame.transform.scale(image, size) for image in jumpimages]
        self.index = 0
        self.image = images[self.index] 

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 0.6
                if self.jumpCount < 1:
                    neg = -0.6
                self.rect.y -= self.jumpCount**2*0.5*neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
                self.rect.y = 440

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        if(self.isJump):
            self.image = self.jumpimages[self.index]
        else:
            self.image = self.images[self.index]


import pygame
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y