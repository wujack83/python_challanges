def is_perfect_number(n):
    divisor = 1

    for i in range(2, int((n / 2)) + 1):
        if n % i == 0:
            divisor += i

    return divisor == n


def calc_perfect_numbers(max_exclusive):

    result = []

    for i in range (2, max_exclusive):
        if is_perfect_number(i):
            result.append(i)

    return result


def calc_perfect_numbers_lc(max_exclusive_n):
    return [i for i in range(2, max_exclusive_n) if is_perfect_number(i)]


def main():

    print(is_perfect_number(6))
    print(is_perfect_number(5))
    print(calc_perfect_numbers(1000))
    print(calc_perfect_numbers(10000))



if __name__ == "__main__":
    main()