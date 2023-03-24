from sortedList import SortedList
import os

os.system("clear")


class Agent:
    def __init__(self):
        self.VALUE_DISTANCE = 1
        self.VALUE_STEP = 1

        self.tiles: list[list[bool]]

        self.explored = dict()
        self.choices = SortedList()

        self.current: self.Coord
        self.start: self.Coord
        self.goal: self.Coord

    def findPath(self, start, goal, tiles):
        self.explored = dict()
        self.choices = SortedList()

        self.tiles = tiles
        self.goal = self.Coord(0, goal, (0, 0), 0)
        self.start = self.Coord(0, start, (0, 0), 0)
        self.current = self.start

        if (self.findPathFromCurrent()):
            return self.getPath()

    def findPathFromCurrent(self):
        while (not self.atGoal()):
            self.addCurrentNeighborsToChoices()
            if (not self.setCurrentToTopChoice()):
                return False  # Choices empty: No path

        return True

    def atGoal(self):
        return self.current == self.goal

    def addCurrentNeighborsToChoices(self):
        r = range(-1, 2)
        for y in r:
            for x in r:
                if (abs(x) == r.stop-1 and abs(y) == r.stop-1):  # Is corner
                    continue

                if ((x, y) != (0, 0)):
                    coord = (x + self.current.COORD[0],
                             y + self.current.COORD[1])

                    coordObj = self.Coord(
                        self.current.STEPS + 1, coord, self.current, self.getValue(coord, True))
                    if (self.validCoord(coord[0], coord[1]) and self.tiles[coord[1]][coord[0]]):
                        if (coordObj in self.explored):
                            if (self.explored[coordObj] > coordObj.STEPS):
                                self.explored.pop(coordObj)
                                self.explored[coordObj] = coordObj.STEPS

                        else:
                            self.explored[coordObj] = coordObj.STEPS
                            self.choices.add(coordObj)

    def validCoord(self, x, y):
        return not (y < 0 or y >= len(self.tiles) or x < 0 or x >= len(self.tiles))

    def getValue(self, coord: tuple, manhattan=False):
        value = (self.current.STEPS + 1) * self.VALUE_STEP

        if (not manhattan):
            value += pow(pow(self.goal.COORD[0] - coord[0], 2) +
                         pow(self.goal.COORD[1] - coord[1], 2), 1/2) * self.VALUE_DISTANCE

        else:
            value += abs(self.goal.COORD[0] - coord[0]) + abs(self.goal.COORD[1] - coord[1]) * self.VALUE_DISTANCE

        return value * -1

    def setCurrentToTopChoice(self):
        if (self.choices.isEmpty()):
            return False

        self.current=self.choices.pop()
        return True

    def getPath(self):
        path=list()
        current=self.current
        while (current != self.start):
            path.append(current.COORD)
            current=current.LAST

        return path

    class Coord:
        def __init__(self, steps: int, coord: tuple[int], last, value: int) -> None:
            self.STEPS=steps
            self.COORD=coord
            self.LAST=last
            self.VALUE=value

        def __eq__(self, other) -> bool:
            return self.COORD == other.COORD

        def __ne__(self, other) -> bool:
            return self.COORD != other.COORD

        def __lt__(self, other):
            return self.VALUE < other.VALUE

        def __le__(self, other):
            self.VALUE <= other.VALUE

        def __gt__(self, other):
            return self.VALUE > other.VALUE

        def __ge__(self, other):
            return self.VALUE >= other.VALUE

        def __hash__(self) -> int:
            return hash(self.COORD)
