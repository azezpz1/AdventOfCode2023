from curses.ascii import isdigit


def decode_line(line: str) -> int:
    """Decodes the value from a given calibration line.
    >>> decode_line("1abc2")
    12
    >>> decode_line("pqr3stu8vwx")
    38
    >>> decode_line("a1b2c3d4e5f")
    15
    >>> decode_line("treb7uchet")
    77
    """
    digits = ""
    for char in line:
        if char.isdigit():
            digits += char
            break
    for char in reversed(line):
        if char.isdigit():
            digits += char
            break
    return int(digits)
