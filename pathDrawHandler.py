import pygame
from grid import Grid
from agent import Agent


class PathDrawHandler:
    def __init__(self, size: int, tileSize: int):
        self.COLOR_BACKGROUND = (200, 200, 200)
        self.COLOR_START = (0, 255, 0)
        self.COLOR_END = (200, 0, 0)
        self.COLOR_WALL = (50, 50, 50)
        self.COLOR_DISCOVERED = (175, 175, 175)
        self.colorPath = [100, 0, 100]
        self.PATH_COLOR_CHANGE = 15

        self.grid = Grid(size, tileSize, self.COLOR_BACKGROUND)
        self.start: tuple[int] = None
        self.end: tuple[int] = None
        self.done = False

        self.tiles = [[True for _ in range(size)] for _ in range(size)]
        self.agent = Agent()

    def draw(self, pos):
        if (self.grid.getColorAt(pos) in (self.COLOR_START, self.COLOR_END)):
            return

        if (not self.start):
            self.start = self.grid.posToIndex(pos)
            self.grid.setColorAt(self.COLOR_START, pos)

        elif (not self.end):
            self.end = self.grid.posToIndex(pos)
            self.grid.setColorAt(self.COLOR_END, pos)

        else:
            column, row = self.grid.posToIndex(pos)
            self.tiles[row][column] = False
            self.grid.setColorAt(self.COLOR_WALL, pos)

    def update(self):
        delay = False

        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_SPACE]):
            self.draw(pygame.mouse.get_pos())
            self.done = False

        elif (pressed[pygame.K_RETURN] and len(self.end) != 0 and not self.done):
            path = self.agent.findPath(self.start, self.end, self.tiles)

            self.__renderExplored(self.agent.explored)
            self.__renderPath(path)
            self.done = True
            delay = False

        elif (pressed[pygame.K_q]):
            self.reset()

        elif (pressed[pygame.K_UP]):
            self.done = False
            max = self.colorPath[0] < self.PATH_COLOR_CHANGE or self.colorPath[2] > 255-self.PATH_COLOR_CHANGE
            if (not max):
                self.agent.VALUE_DISTANCE += 1
                self.colorPath[0] = self.colorPath[0] + \
                    self.PATH_COLOR_CHANGE if self.colorPath[0] <= 255-self.PATH_COLOR_CHANGE else 255
                self.colorPath[2] = self.colorPath[2] - \
                    self.PATH_COLOR_CHANGE if self.colorPath[2] >= self.PATH_COLOR_CHANGE else 0

            delay = True

        elif (pressed[pygame.K_DOWN]):
            self.done = False
            max = self.colorPath[0] < self.PATH_COLOR_CHANGE or self.colorPath[2] > 255-self.PATH_COLOR_CHANGE
            if (not max):
                self.agent.VALUE_DISTANCE -= 1
                self.colorPath[0] = self.colorPath[0] - \
                    self.PATH_COLOR_CHANGE if self.colorPath[0] >= self.PATH_COLOR_CHANGE else 0
                self.colorPath[2] = self.colorPath[2] + \
                    self.PATH_COLOR_CHANGE if self.colorPath[2] <= 255-self.PATH_COLOR_CHANGE else 255

            delay = True
        
        return delay

    def render(self, screen: pygame.Surface):
        self.grid.render(screen)

    def __renderPath(self, path: list[tuple[int]]):
        if (path and len(path)):
            for coord in path:
                self.grid.setColorAt(
                    self.colorPath, self.grid.indexToPos(coord[0], coord[1]))

    def __renderExplored(self, path):
        if (path and len(path)):
            for coord in path:
                if (self.grid.getColorAt(self.grid.indexToPos(coord.COORD[0], coord.COORD[1])) == self.COLOR_BACKGROUND):
                    self.grid.setColorAt(
                        self.COLOR_DISCOVERED, self.grid.indexToPos(coord.COORD[0], coord.COORD[1]))

    def reset(self):
        self.grid.reset()
        self.agent = Agent()
        self.colorPath = [100, 0, 100]

        for row in range(len(self.tiles)):
            for column in range(len(self.tiles)):
                if (not self.tiles[row][column]):
                    self.grid.setColorAt(
                        self.COLOR_WALL, self.grid.indexToPos(column, row))

        self.grid.setColorAt(self.COLOR_START, self.grid.indexToPos(
            self.start[0], self.start[1]))
        self.grid.setColorAt(
            self.COLOR_END, self.grid.indexToPos(self.end[0], self.end[1]))

        self.done = False
