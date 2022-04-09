def calc_checksum(input):
    result = 0
    for i in range(len(input)):
        result += ((i + 1) * int(input[i]))
    return result % 10


def calc_checksum_v2(input):
    result = 0

    for i, current_char in enumerate(input):
        result += (int(current_char)) * (i + 1)
    return result % 10


def main():
    print(calc_checksum("11111"))


if __name__ == "__main__":
    main()