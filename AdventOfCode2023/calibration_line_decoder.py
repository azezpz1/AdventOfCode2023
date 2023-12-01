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
    >>> decode_line("two1nine")
    29
    >>> decode_line("eightwothree")
    83
    >>> decode_line("abcone2threexyz")
    13
    >>> decode_line("xtwone3four")
    24
    >>> decode_line('4nineeightseven2")
    42
    >>> decode_line("zoneight234")
    14
    >>> decode_line("7pqrstsixteen")
    76
    """
    digits = get_first_digit(line) + get_first_digit(line, True)
    return int(digits)


def get_first_digit(line: str, is_reversed=False) -> str:
    if is_reversed:
        line = line[::-1]
    for char in line:
        if char.isdigit():
            return char
    return ""
