from pathlib import Path

import calibration_line_decoder


def main():
    total = get_calibration_amount()
    print(total)


def get_calibration_amount():
    directory = Path(__file__).parent.absolute()
    calibration_data_path = directory / "inputs" / "calibration_data.txt"
    with open(calibration_data_path) as f:
        total = 0
        for line in f:
            total += calibration_line_decoder.decode_line(line)
    return total


if __name__ == "__main__":
    main()
