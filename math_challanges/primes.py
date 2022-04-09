def is_prime(potential_prime):
    for number in range(2, int(potential_prime / 2) + 1):
        if potential_prime % number == 0:
            return False
    return True


def calc_primes_up_to(max_value):
    result = []

    for i in range(2, max_value + 1):
        if is_prime(i):
            result.append(i)
    return result


def is_twin_pair(n):
    return is_prime(n) and is_prime(n + 2)


def is_cousin(n):
    return is_prime(n) and is_prime(n + 4)


def is_sexy_pair(n):
    return is_prime(n) and is_prime(n + 6)


def calc_primes_up_to(max_number):

    twin_pairs = {number: number + 2 for number in range(1, max_number) if is_twin_pair(number)}
    cousin_pairs = {number: number + 4 for number in range(1, max_number) if is_cousin(number)}
    sexy_pairs = {number: number + 6 for number in range(1, max_number) if is_sexy_pair(number)}

    print("Twins: ", twin_pairs)
    print("Cousins: ", cousin_pairs)
    print("Sexy: ", sexy_pairs)


def main():
    print(calc_primes_up_to(50))


if __name__ == "__main__":
    main()