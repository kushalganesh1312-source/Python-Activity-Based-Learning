# Case Study 27: Advanced Numeric Pattern Generator
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: nested loops, if-else, operators, string handling, validation


def hollow_diamond(n):
    # n must be odd and >= 3
    if n < 3 or n % 2 == 0:
        print("  INVALID: size %d -> must be odd and >= 3" % n)
        return False

    mid = n // 2
    for i in range(n):
        dist = i - mid
        if dist < 0:
            dist = -dist
        digit = str(mid - dist + 1)
        row_len = 2 * (mid - dist) + 1
        pad = (n - row_len) // 2
        line = ""
        for j in range(row_len):
            if j == 0 or j == row_len - 1:
                line = line + digit
            else:
                line = line + " "
        print(" " * pad + line)
    return True


def number_pyramid(m):
    # m must be >= 1
    if m < 1:
        print("  INVALID: size %d -> must be >= 1" % m)
        return False
    for i in range(1, m + 1):
        line = ""
        for j in range(1, i + 1):
            line = line + str(j)
        for j in range(i - 1, 0, -1):
            line = line + str(j)
        print(" " * (m - i) + line)
    return True


def main():
    print("=" * 44)
    print("  NUMERIC PATTERN GENERATOR")
    print("=" * 44)

    print("\nHollow diamond, size 5")
    print("-" * 44)
    hollow_diamond(5)

    print("\nHollow diamond, size 7")
    print("-" * 44)
    hollow_diamond(7)

    print("\nValidation: even size 6")
    print("-" * 44)
    hollow_diamond(6)

    print("\nValidation: size 1")
    print("-" * 44)
    hollow_diamond(1)

    print("\nNumber pyramid, size 5")
    print("-" * 44)
    number_pyramid(5)

    print("\nValidation: size -2")
    print("-" * 44)
    number_pyramid(-2)

    print("\nDone. All sizes were checked before printing.")


if __name__ == "__main__":
    main()
