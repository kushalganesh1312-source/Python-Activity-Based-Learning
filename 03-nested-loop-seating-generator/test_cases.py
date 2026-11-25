# Test cases for Case Study 26 - Nested Loop Seating Generator
# Name: BOPPUDI KARTHIK, Roll No: 26000451
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "sol", os.path.join(os.path.dirname(__file__), "solution.py"))
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)

passed = 0


def check(label, condition):
    global passed
    assert condition, "FAILED: " + label
    passed = passed + 1
    print("  PASS:", label)


seat = sol.build_seating()

# TC-01: grid size 5x6
check("grid has 5 rows", len(seat) == 5)
check("each row has 6 columns", len(seat[0]) == 6)

# TC-02: reserved seats are marked R
check("seat (1,1) is reserved", seat[0][0] == "R")
check("seat (3,4) is reserved", seat[2][3] == "R")
check("seat (5,6) is reserved", seat[4][5] == "R")

# TC-03: alternate rows block odd columns
check("row 2 col 1 blocked", seat[1][0] == "X")
check("row 2 col 3 blocked", seat[1][2] == "X")
check("row 4 col 5 blocked", seat[3][4] == "X")

# TC-04: alternate rows allow even columns
check("row 2 col 2 open", seat[1][1] == "O")
check("row 4 col 6 open", seat[3][5] == "O")

# TC-05: normal rows are open except reserved
check("row 1 col 2 open", seat[0][1] == "O")
check("row 3 col 1 open", seat[2][0] == "O")

# TC-06: counts add up to total
o, r, x = sol.count_seats(seat)
check("counts add up to 30", o + r + x == 30)
check("reserved count is 3", r == 3)
# blocked: 2 rows x 3 cols = 6
check("blocked count is 6", x == 6)
check("open count is 21", o == 21)

# TC-07: reserved validation passes for valid seats
check("no validation problems", len(sol.check_reserved()) == 0)

print("\nAll %d tests passed for Case Study 26" % passed)
