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
    >>> decode_line("4nineeightseven2")
    42
    >>> decode_line("zoneight234")
    14
    >>> decode_line("7pqrstsixteen")
    76
    """
    first = ""
    last = ""
    index_of_first = 0
    index_of_last = 0

    index = 0
    for index in range(len(line)):
        number_at_index = get_number_from_index(index, line)
        if first == "":
            first = number_at_index
            index_of_first = index
        if number_at_index != "":
            last = number_at_index
            index_of_last = index

    return int(first + last)


def get_number_from_index(index: int, line: str) -> str:
    """Gets the number (either because it's a digit or the word) from the given index

    Args:
        index (int): The index to check for the number at.
        line (str): The string that contains numbers

    Returns:
        str: A string representation of the number that was found (e.g. "1", "2", etc.)

    >>> get_number_from_index(0, "123")
    '1'
    >>> get_number_from_index(1, "123")
    '2'
    >>> get_number_from_index(0, "a12")
    ''
    >>> get_number_from_index(0, "one")
    '1'
    >>> get_number_from_index(3, "onetwo")
    '2'
    """
    possible_number_strings = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    if line[index].isdigit():
        return line[index]
    else:
        for key, value in possible_number_strings.items():
            potential_number_string = line[index : index + len(key)]
            if key == potential_number_string:
                return value
    return ""
