import math


def combinatorics():
    values = []
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                if a**2 + b**2 == c**2:
                    values.append((a,b,c))
    return values


def combinatorics_on2():

    for a in range(1, 100):
        for b in range(1, 100):
            c = int(math.sqrt(a**2 + b**2))
            if c < 100 and a**2 + b**2 == c**2:
                print("a =", a, "/ b= ", b, "/ c=", c)


def combinatorics_2():
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                for d in range(1,100):
                    if a**2 + b**2 == c**2 + d**2:
                        print("a =", a, "/ b= ", b, "/ c=", c, "/ d=", d)


def combinatorics_2_o3():
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                value = a**2 + b**2 - c**2
                if value > 0:
                    d = int(math.sqrt(a**2 + b**2 - c**2))
                    if d < 100 and a**2 + b**2 == c**2 + d **2:
                        print("a =", a, "/ b= ", b, "/ c=", c, " /d=", d)

def main():
    #print(combinatorics())
    #print(combinatorics_on2())

    print(combinatorics_2_o3())


if __name__ == "__main__":
    main()
