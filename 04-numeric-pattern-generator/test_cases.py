# Test cases for Case Study 27 - Advanced Numeric Pattern Generator
# Name: BOPPUDI KARTHIK, Roll No: 26000451
import importlib.util
import io
import os
from contextlib import redirect_stdout

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


def capture(func, arg):
    buf = io.StringIO()
    with redirect_stdout(buf):
        result = func(arg)
    return result, buf.getvalue()


# TC-01: valid diamond size 5 returns True
ok, out = capture(sol.hollow_diamond, 5)
check("diamond size 5 accepted", ok == True)

# TC-02: diamond size 5 has 5 lines
lines = out.strip().split("\n")
check("diamond size 5 has 5 lines", len(lines) == 5)

# TC-03: middle line of size 5 diamond is "33333" (no spaces, full row)
check("middle line is 3   3", lines[2].strip() == "3   3")

# TC-04: even size rejected
ok, out = capture(sol.hollow_diamond, 6)
check("even size 6 rejected", ok == False and "INVALID" in out)

# TC-05: size 1 rejected (too small)
ok, out = capture(sol.hollow_diamond, 1)
check("size 1 rejected", ok == False)

# TC-06: valid pyramid size 4
ok, out = capture(sol.number_pyramid, 4)
check("pyramid size 4 accepted", ok == True)
lines = out.strip().split("\n")
check("pyramid size 4 has 4 lines", len(lines) == 4)
check("last pyramid line is 1234321", lines[3].strip() == "1234321")

# TC-07: pyramid size 0 rejected
ok, out = capture(sol.number_pyramid, 0)
check("pyramid size 0 rejected", ok == False)

# TC-08: pyramid negative rejected
ok, out = capture(sol.number_pyramid, -3)
check("pyramid size -3 rejected", ok == False)

print("\nAll %d tests passed for Case Study 27" % passed)
