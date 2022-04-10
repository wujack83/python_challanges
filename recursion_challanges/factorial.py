def factorial(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1:
        return 1

    #rekursiver abstieg

    return n * factorial(n - 1)


# Als Lambda Funktion
factorial_ = lambda n: n if n == 1 else n * factorial_(n - 1)


def main():
    print(factorial(5))
    print(factorial_(5))


if __name__ == "__main__":
    main()
