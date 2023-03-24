import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x=0, y=0):
        super().__init__()
        self.image = pygame.Surface([width, height])

        self.color = color
        self.width = width
        self.height = height

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

    def update(self, color):
        self.setColor(color)