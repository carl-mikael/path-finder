import os

os.system("clear")


class SortedList:
    def __init__(self):
        self.first = self.Item
        self.count = 0

    def add(self, value):
        item = self.Item(value)
        if (self.isEmpty()):
            self.first = item
            self.count += 1
            return

        if (item > self.first):
            item.Next = self.first
            self.first = item
            self.count += 1
            return

        current = self.first
        while (current and current > item and not (not current.Next or current.Next <= item)):
            current = current.Next


        if (current and current == item or current and current.Next and current.Next == item):
            return

        item.Next = current.Next
        current.Next = item
        self.count += 1

    def remove(self, value):
        if (self.isEmpty()):
            return

        if (self.first == value):
            self.first = self.first.Next
            self.count -= 1
            return

        current = self.first
        while (current and current > value and not (not current.Next or current.Next <= value)):
            current = current.Next

        current.Next = current.Next.Next
        self.count -= 1

    def isEmpty(self):
        return self.count == 0

    def pop(self):
        value = self.first.VALUE
        self.first = self.first.Next
        self.count -= 1
        return value

    def __str__(self):
        if (self.isEmpty()):
            return ""

        if (self.count == 1):
            return str(self.first.VALUE)

        strBuilder = list()
        current = self.first
        while (current):
            strBuilder.extend((", ", str(current.VALUE)))
            current = current.Next

        strBuilder.remove(", ")
        return str().join(strBuilder)

    def __len__(self):
        return self.count

    class Item:
        def __init__(self, value: int, next=None) -> None:
            self.VALUE = value
            self.Next = next

        def __gt__(self, other: int):
            return self.VALUE > other.VALUE

        def __ge__(self, other):
            return self.VALUE >= other.VALUE

        def __lt__(self, other: int):
            return self.VALUE < other.VALUE

        def __le__(self, other):
            return self.VALUE <= other.VALUE

        def __eq__(self, other) -> bool:
            return self.VALUE == other.VALUE

        def __ne__(self, other):
            return self.VALUE != other.VALUE


def main():
    sl = SortedList()

    sl.add(1)
    sl.add(2)
    sl.add(1)

    print(sl)

    assert sl.count == 2
    assert sl.isEmpty() == False
    assert sl.pop() == 2
    assert sl.count == 1


if (__name__ == "__main__"):
    main()
