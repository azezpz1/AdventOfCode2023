from AdventOfCode2023.cube_bag_result_parser import parse_game_from_line


def test_parse_game_from_line():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    game = parse_game_from_line(line)

    assert game.grabs[0].red == 4
    assert game.grabs[0].green == 0
    assert game.grabs[0].blue == 3
    assert game.grabs[1].red == 1
    assert game.grabs[1].green == 2
    assert game.grabs[1].blue == 6
    assert game.grabs[2].red == 0
    assert game.grabs[2].green == 2
    assert game.grabs[2].blue == 0
