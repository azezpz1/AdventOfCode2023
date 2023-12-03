from pathlib import Path

from AdventOfCode2023 import calibration_line_decoder
from AdventOfCode2023.cube_bag_result_parser import parse


def main():
    total = get_minimum_power_total()
    print(total)


def get_id_total():
    games = get_games()
    total = 0
    for index, game in enumerate(games, start=1):
        print(
            f"from game: {index}:{game.total_red},{game.total_green},{game.total_blue}"
        )
        if game.is_possible:
            total += index
    return total


def get_games():
    directory = Path(__file__).parent.absolute()
    cube_data_path = directory / "AdventOfCode2023" / "inputs" / "cube_data.txt"
    games = parse(cube_data_path)
    return games


def get_minimum_power_total() -> int:
    games = get_games()
    total_power = 0
    for game in games:
        total_power += game.minimum_power
    return total_power


if __name__ == "__main__":
    main()
