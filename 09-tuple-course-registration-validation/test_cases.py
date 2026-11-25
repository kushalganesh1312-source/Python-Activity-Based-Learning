# Test cases for Case Study 64 - Tuple-Based Course Registration Validation
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


# TC-01: Karthik valid
problems = sol.validate(sol.REGISTRATIONS[0])
check("R01 Karthik valid", len(problems) == 0)

# TC-02: Priya duplicate CS101
problems = sol.validate(sol.REGISTRATIONS[1])
found = False
for p in problems:
    if "duplicate" in p and "CS101" in p:
        found = True
check("R02 Priya duplicate reported", found == True)

# TC-03: Ravi missing prerequisite CS101 for CS201
problems = sol.validate(sol.REGISTRATIONS[2])
found = False
for p in problems:
    if "prerequisite" in p:
        found = True
check("R03 Ravi missing prerequisite", found == True)

# TC-04: Sneha too many courses (5 > 4) and exclusive pair
problems = sol.validate(sol.REGISTRATIONS[3])
found_max = False
found_excl = False
for p in problems:
    if "max" in p:
        found_max = True
    if "exclusive" in p:
        found_excl = True
check("R04 Sneha too many courses", found_max == True)
check("R04 Sneha exclusive pair", found_excl == True)

# TC-05: Arjun valid (CS101 + CS201 together)
problems = sol.validate(sol.REGISTRATIONS[4])
check("R05 Arjun valid", len(problems) == 0)

# TC-06: Divya missing CS201 for CS301
problems = sol.validate(sol.REGISTRATIONS[5])
found = False
for p in problems:
    if "CS201" in p:
        found = True
check("R06 Divya missing CS201", found == True)

# TC-07: unknown code detection
bad = ("R99", "Test", (("XYZ999", "Fake Course"),))
problems = sol.validate(bad)
found = False
for p in problems:
    if "unknown" in p:
        found = True
check("unknown code detected", found == True)

# TC-08: counts - 2 valid (R01, R05), 4 invalid
valid = 0
for s in sol.REGISTRATIONS:
    if len(sol.validate(s)) == 0:
        valid = valid + 1
check("2 valid, 4 invalid", valid == 2 and len(sol.REGISTRATIONS) - valid == 4)

print("\nAll %d tests passed for Case Study 64" % passed)
