import pytest
from AdventOfCode2023.cube_bag_result_parser import parse_game_from_line


@pytest.mark.parametrize(
    "test_input,expected_red,expected_green,expected_blue",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 5, 4, 9),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 1, 6, 6),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            25,
            26,
            11,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            23,
            7,
            21,
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 7, 5, 3),
        ("Game 95: 6 blue, 1 green; 3 red, 11 green; 4 blue", 3, 12, 10),
    ],
)
def test_parse_game_from_line(test_input, expected_red, expected_green, expected_blue):
    game = parse_game_from_line(test_input)

    assert game.total_red == expected_red
    assert game.total_green == expected_green
    assert game.total_blue == expected_blue
