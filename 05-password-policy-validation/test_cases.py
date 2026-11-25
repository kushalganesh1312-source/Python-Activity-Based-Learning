# Test cases for Case Study 29 - Password Policy Validation Engine
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


# TC-01: strong password passes
errors = sol.validate_password("Campus#2026")
check("Campus#2026 passes", len(errors) == 0)

# TC-02: short password fails length
errors = sol.validate_password("hello")
found = False
for e in errors:
    if "length" in e:
        found = True
check("short password fails length check", found == True)

# TC-03: missing uppercase
errors = sol.validate_password("campus#2026")
found = False
for e in errors:
    if "uppercase" in e:
        found = True
check("missing uppercase reported", found == True)

# TC-04: missing digit
errors = sol.validate_password("Campus#Abc")
found = False
for e in errors:
    if "digit" in e:
        found = True
check("missing digit reported", found == True)

# TC-05: missing special
errors = sol.validate_password("Campus2026")
found = False
for e in errors:
    if "special" in e:
        found = True
check("missing special reported", found == True)

# TC-06: prohibited word admin
errors = sol.validate_password("admin@123")
found = False
for e in errors:
    if "prohibited" in e:
        found = True
check("prohibited word admin reported", found == True)

# TC-07: repeat check - aaa should fail
check("aaa repeat detected", sol.has_repeat("aaaBBB111!!!") == True)
check("no repeat in Campus#2026", sol.has_repeat("Campus#2026") == False)

# TC-08: Karthik$99 passes
errors = sol.validate_password("Karthik$99")
check("Karthik$99 passes", len(errors) == 0)

print("\nAll %d tests passed for Case Study 29" % passed)
