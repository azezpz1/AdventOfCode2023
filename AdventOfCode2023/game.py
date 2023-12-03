import typing
from AdventOfCode2023.grab import Grab


class Game:
    def __init__(self) -> None:
        self.grabs: typing.List[Grab] = []

    def add(self, grab: Grab):
        self.grabs.append(grab)

    @property
    def is_possible(self) -> bool:
        for grab in self.grabs:
            if grab.red > 12 or grab.green > 13 or grab.blue > 14:
                return False
        return True

    @property
    def minimum_possible_values(self) -> typing.Tuple[int, int, int]:
        min_red = 0
        min_green = 0
        min_blue = 0
        for grab in self.grabs:
            if grab.red > min_red:
                min_red = grab.red
            if grab.green > min_green:
                min_green = grab.green
            if grab.blue > min_blue:
                min_blue = grab.blue
        return (min_red, min_green, min_blue)

    @property
    def minimum_power(self) -> int:
        red, green, blue = self.minimum_possible_values
        return red * green * blue

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
