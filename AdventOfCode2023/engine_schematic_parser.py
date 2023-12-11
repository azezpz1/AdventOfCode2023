from pathlib import Path
import typing


def parse(path: Path) -> typing.Dict[str, typing.List[str]]:
    """Parses an engine schematic.

    Args:
        path (Path): Path to the engine schematic.

    Returns:
        typing.Dict[str, typing.List[str]]: Keys are "partNumbers", "notPartNumbers"
    """

    with open(path) as f:
        file_lines = f.readlines()