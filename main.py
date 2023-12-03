from pathlib import Path

from AdventOfCode2023 import calibration_line_decoder
from AdventOfCode2023.cube_bag_result_parser import parse


def main():
    total = get_id_total()
    print(total)


def get_id_total():
    directory = Path(__file__).parent.absolute()
    cube_data_path = directory / "AdventOfCode2023" / "inputs" / "cube_data.txt"
    games = parse(cube_data_path)
    total = 0
    for index, game in enumerate(games, start=1):
        print(
            f"from game: {index}:{game.total_red},{game.total_green},{game.total_blue}"
        )
        if game.is_possible:
            total += index
    return total


if __name__ == "__main__":
    main()
