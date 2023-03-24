from pygame import sprite, Surface
from square import Square
import pygame


class Grid:
    def __init__(self, sideLenght: int, tileSideLenght: int, color: pygame.Color):
        self.tiles = sprite.Group()
        self.SIDE_LENGHT = sideLenght
        self.TILE_SIDE_LENGHT = tileSideLenght
        self.COLOR_BACKGROUND = color

        self.initTiles()

    def initTiles(self):
        for i in range(self.SIDE_LENGHT):
            for j in range(self.SIDE_LENGHT):
                tile = Square(self.COLOR_BACKGROUND, self.TILE_SIDE_LENGHT, self.TILE_SIDE_LENGHT,
                              j * self.TILE_SIDE_LENGHT, i * self.TILE_SIDE_LENGHT)
                self.tiles.add(tile)

    def render(self, surface: Surface):
        self.tiles.draw(surface)

    def validCoord(self, pos):
        row, column = pos[1] // self.TILE_SIDE_LENGHT, pos[0] // self.TILE_SIDE_LENGHT
        return not (row >= self.SIDE_LENGHT or row < 0 or column >= self.SIDE_LENGHT or column < 0)

    def __posToIndex(self, pos):
        if (not self.validCoord(pos)):
            return -1

        return pos[1] // self.TILE_SIDE_LENGHT * self.SIDE_LENGHT + pos[0] // self.TILE_SIDE_LENGHT

    def posToIndex(self, pos):
        if (not self.validCoord(pos)):
            return -1

        return pos[0] // self.TILE_SIDE_LENGHT, pos[1] // self.TILE_SIDE_LENGHT

    def indexToPos(self, x, y):
        return x * self.TILE_SIDE_LENGHT, y * self.TILE_SIDE_LENGHT

    def setColorAt(self, color: pygame.Color, pos):
        index = self.__posToIndex(pos)
        if (index == -1):
            return False

        self.tiles.sprites()[index].setColor(color)
        return True

    def getColorAt(self, pos):
        index = self.__posToIndex(pos)
        if (index == -1):
            return (0, 0, 0)

        return self.tiles.sprites()[index].getColor()

    def reset(self):
        self.tiles.update(self.COLOR_BACKGROUND)

    def __len__(self):
        return len(self.tiles)
