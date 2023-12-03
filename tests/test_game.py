from AdventOfCode2023.game import Game
from AdventOfCode2023.grab import Grab


def test_total_red():
    game = Game()
    game.add(Grab(1, 1, 0))
    game.add(Grab(3, 1, 1))

    total = game.total_red

    assert total == 4


def test_total_green():
    game = Game()
    game.add(Grab(1, 1, 0))
    game.add(Grab(3, 1, 1))

    total = game.total_green

    assert total == 2


def test_total_blue():
    game = Game()
    game.add(Grab(1, 1, 0))
    game.add(Grab(3, 1, 1))

    total = game.total_blue

    assert total == 1


def test_maximum_is_possible_returnstrue():
    game = Game()
    game.add(Grab(12, 13, 14))

    assert game.is_possible


def test_overred_is_possible_returnsfalse():
    game = Game()
    game.add(Grab(13, 13, 14))

    assert not game.is_possible


def test_overgreen_is_possible_returnsfalse():
    game = Game()
    game.add(Grab(12, 14, 14))

    assert not game.is_possible


def test_overblue_is_possible_returnsfalse():
    game = Game()
    game.add(Grab(12, 13, 15))

    assert not game.is_possible
