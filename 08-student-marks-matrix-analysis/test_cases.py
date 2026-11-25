# Test cases for Case Study 42 - Student Marks Matrix Analysis
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


# TC-01: matrix size 4x4
check("4 students", len(sol.STUDENTS) == 4)
check("4 subjects", len(sol.SUBJECTS) == 4)
check("marks has 4 rows", len(sol.MARKS) == 4)
check("each row has 4 marks", len(sol.MARKS[0]) == 4)

# TC-02: Karthik total = 78+82+75+85 = 320
total = 0
for m in sol.MARKS[0]:
    total = total + m
check("Karthik total 320", total == 320)

# TC-03: Ravi total = 85+80+88+90 = 343, highest
total = 0
for m in sol.MARKS[2]:
    total = total + m
check("Ravi total 343", total == 343)

# TC-04: grades
check("grade A for 85+", sol.grade_of(86) == "A (Distinction)")
check("grade B for 70-84", sol.grade_of(75) == "B (First Class)")
check("grade C for 55-69", sol.grade_of(60) == "C (Second Class)")
check("grade D below 55", sol.grade_of(50) == "D (Third Class)")

# TC-05: Maths column average = (78+62+85+70)/4 = 73.75
total = 0
for r in range(4):
    total = total + sol.MARKS[r][0]
avg = total / 4
check("Maths average 73.75", abs(avg - 73.75) < 0.01)

# TC-06: highest mark is 90 (Ravi in CS)
high = -1
for r in range(4):
    for c in range(4):
        if sol.MARKS[r][c] > high:
            high = sol.MARKS[r][c]
check("highest mark 90", high == 90)

# TC-07: lowest mark is 58 (Priya in Physics)
low = 101
for r in range(4):
    for c in range(4):
        if sol.MARKS[r][c] < low:
            low = sol.MARKS[r][c]
check("lowest mark 58", low == 58)

print("\nAll %d tests passed for Case Study 42" % passed)
