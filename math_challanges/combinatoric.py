def combinatorics():
    values = []
    for a,b in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                if a**2 + b**2 == c**2:
                    values.append((a,b,c))
    return values


def main():
    print(combinatorics())


if __name__ == "__main__":
    main()
