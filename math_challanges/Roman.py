def from_roman_number(roman_number: str) -> int:
    value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    last_digit_value = 0

    for roman_digit in reversed(roman_number):
        digit_value = value_map[roman_digit]
        add_mode = digit_value >= last_digit_value

        if add_mode:
            result += digit_value
            last_digit_value = digit_value
        else:
            result -= digit_value

    return result


def to_roman_number(value):

    value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    


def main():
    print(from_roman_number("VI"))
    print(from_roman_number("IV"))


if __name__ == "__main__":
    main()

