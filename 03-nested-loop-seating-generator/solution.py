# Case Study 26: Nested Loop Examination Seating Generator
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: nested loops, if-else, lists (nested list), operators

ROWS = 5
COLS = 6
# reserved seats as tuples (row, col), 1-based
RESERVED = [(1, 1), (3, 4), (5, 6)]
# in these rows only even columns are allowed (alternate seating)
ALT_ROWS = (2, 4)
ALT_BLOCKED = (1, 3, 5)


def check_reserved():
    problems = []
    for r, c in RESERVED:
        if r < 1 or r > ROWS or c < 1 or c > COLS:
            problems.append("seat (%d,%d) is outside the %dx%d grid" % (r, c, ROWS, COLS))
    return problems


def build_seating():
    # nested list: O = open, R = reserved, X = blocked
    seat = []
    for r in range(1, ROWS + 1):
        row = []
        for c in range(1, COLS + 1):
            if (r, c) in RESERVED:
                row.append("R")
            elif r in ALT_ROWS and c in ALT_BLOCKED:
                row.append("X")
            else:
                row.append("O")
        seat.append(row)
    return seat


def print_seating(seat):
    print("     " + "  ".join("C%d" % c for c in range(1, COLS + 1)))
    print("     " + "-" * (COLS * 3 - 1))
    for r in range(ROWS):
        cells = "  ".join(seat[r][c] for c in range(COLS))
        print("R%-3d | %s" % (r + 1, cells))
    print("\n  O = open seat, R = reserved, X = blocked (alternate rule)")


def count_seats(seat):
    open_count = 0
    reserved_count = 0
    blocked_count = 0
    for row in seat:
        for cell in row:
            if cell == "O":
                open_count = open_count + 1
            elif cell == "R":
                reserved_count = reserved_count + 1
            else:
                blocked_count = blocked_count + 1
    return open_count, reserved_count, blocked_count


def main():
    print("=" * 56)
    print("  EXAMINATION SEATING ARRANGEMENT")
    print("=" * 56)

    problems = check_reserved()
    if len(problems) > 0:
        print("Validation errors found:")
        for p in problems:
            print("  - " + p)
        return

    seat = build_seating()
    print_seating(seat)

    o, r, x = count_seats(seat)
    print("\nSummary")
    print("-" * 56)
    print("  Total positions : %d (%d rows x %d cols)" % (ROWS * COLS, ROWS, COLS))
    print("  Open seats (O)  : %d" % o)
    print("  Reserved (R)    : %d" % r)
    print("  Blocked (X)     : %d" % x)
    print("  Capacity        : %d students" % (o + r))

    # demo: check a seat outside the grid
    print("\nValidation demo:")
    bad_row = 7
    bad_col = 2
    if bad_row >= 1 and bad_row <= ROWS and bad_col >= 1 and bad_col <= COLS:
        print("  seat (%d,%d) accepted" % (bad_row, bad_col))
    else:
        print("  ERROR: seat (%d,%d) is outside %dx%d grid" % (bad_row, bad_col, ROWS, COLS))


if __name__ == "__main__":
    main()
