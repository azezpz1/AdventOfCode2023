import typing
from AdventOfCode2023.grab import Grab


class Game:
    def __init__(self) -> None:
        self.grabs: typing.List[Grab] = []

    def add(self, grab: Grab):
        self.grabs.append(grab)

    @property
    def total_red(self):
        total = 0
        for grab in self.grabs:
            total += grab.red
        return total

    @property
    def total_green(self):
        total = 0
        for grab in self.grabs:
            total += grab.green
        return total

    @property
    def total_blue(self):
        total = 0
        for grab in self.grabs:
            total += grab.blue
        return total
