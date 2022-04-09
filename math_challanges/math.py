def calc(m, n):
    return m * n // 2 % 7


def calc_sum_and_count_all_numbers_div_by_2_or_7_v2(max_exclusive):
    count = 0
    sum = 0

    for i in range(1, max_exclusive):
        is_divisible_by2or7 = i % 2 == 0 or i % 7 == 0
        if is_divisible_by2or7:
            count += 1
            sum += i

    return {"sum": sum, "count": count}


def is_even(n):
    return n%2 == 0


def is_odd(n):
    return n%2 != 0

value_text_mapping = {
    1: "ONE", 2: "TWO", 3: "THREE", 4 : "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}


def number_as_text(n):
    value = ""
    remaining_value = n

    while remaining_value > 0:
        remainder_as_text = digit_as_text(remaining_value % 10)
        remaining_value = int(remaining_value / 10)
        value = remainder_as_text + " " + value

    return value.strip()

def digit_as_text(n):
    return value_text_mapping[n % 10]


def number_as_text_short(n):
    value = ""
    for ch in str(n):
        value += digit_as_text(int(ch)) + " "
    return value.strip()


def main():

    print(calc_sum_and_count_all_numbers_div_by_2_or_7_v2(10))
    print(is_even(4))
    print(is_even(5))
    print(number_as_text(78))
    print(number_as_text_short(77))


if __name__ == "__main__":
    main()
