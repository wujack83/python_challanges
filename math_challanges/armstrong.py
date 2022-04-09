def calc_armstrong_numbers():
    results = []
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                if 100 * a + 10 * b + c == a ** 3 + b ** 3 + c ** 3:
                    results.append(100 * a + 10 * b + c)
    return results


def calc_armstrong_numbers_generic(x,y,z):
    results = []
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                if 100 * a + 10 * b + c == a ** x + b ** y + c ** z:
                    results.append(100 * a + 10 * b + c)
    return results


def main():
    calc_armstrong_numbers()
    print("----------------------------------------------------------")
    calc_armstrong_numbers_generic(3,3,3)
    print("----------------------------------------------------------")
    calc_armstrong_numbers_generic(1,2,3)
    print("----------------------------------------------------------")
    calc_armstrong_numbers_generic(3,2,1)


if __name__ == "__main__":
    main()