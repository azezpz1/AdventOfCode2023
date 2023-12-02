from io import UnsupportedOperation
import pathlib
import typing

from AdventOfCode2023.game import Game
from AdventOfCode2023.grab import Grab


def parse(path_to_results: pathlib.Path) -> typing.List[Game]:
    games: typing.List[Game] = []
    with open(path_to_results) as f:
        for line in f:
            parse_game_from_line(line)
    return games


def parse_game_from_line(line: str) -> Game:
    """Parses game information from a string

    Args:
        line (str): Line containing game information.

    Raises:
        UnsupportedOperation: If an invalid color is found in the line.

    Returns:
        Game: Data for a game.
    """
    game = Game()
    data = line.split(": ")[1]
    raw_grabs = data.split(";")
    for raw_grab in raw_grabs:
        red = 0
        green = 0
        blue = 0
        raw_grab = raw_grab.strip()
        raw_colors = raw_grab.split(", ")
        for raw_color in raw_colors:
            amount, color = raw_color.split(" ", maxsplit=2)
            amount = int(amount)
            if color == "red":
                red = amount
            elif color == "green":
                green = amount
            elif color == "blue":
                blue = amount
            else:
                raise UnsupportedOperation(f"Unknown color {color}")
        game.add(Grab(red, green, blue))
    return game
