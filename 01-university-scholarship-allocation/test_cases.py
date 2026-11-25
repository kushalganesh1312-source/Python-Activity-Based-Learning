# Test cases for Case Study 01 - University Scholarship Allocation
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


# TC-01: Karthik should be eligible, aggregate 80.0
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[0])
check("S201 Karthik eligible with aggregate 80.0", ok == True and abs(agg - 80.0) < 0.01 and reasons == [])

# TC-02: Priya aggregate below 65
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[1])
check("S202 Priya rejected, aggregate 58.0 below 65", ok == False and abs(agg - 58.0) < 0.01)

# TC-03: Priya subject minimum failure (Physics 48)
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[1])
found = False
for r in reasons:
    if "Physics" in r:
        found = True
check("S202 subject failure reported for Physics", found == True)

# TC-04: Lakshmi income failure
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[7])
found = False
for r in reasons:
    if "income" in r:
        found = True
check("S208 Lakshmi rejected for income", ok == False and found == True)

# TC-05: Manoj attendance failure
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[6])
found = False
for r in reasons:
    if "attendance" in r:
        found = True
check("S207 Manoj rejected for attendance 70%", ok == False and found == True)

# TC-06: ranking - Ravi should be first
eligible = []
for a in sol.APPLICANTS:
    ok, agg, _ = sol.check_applicant(a)
    if ok:
        eligible.append((a[0], a[1], round(agg, 2), a[3], a[4]))
eligible.sort(key=sol.rank_key)
check("S203 Ravi ranked first", eligible[0][0] == "S203")

# TC-07: tie at 70.0 between Sneha and Arjun, Arjun higher attendance so first
idx_sneha = -1
idx_arjun = -1
for i in range(len(eligible)):
    if eligible[i][0] == "S204":
        idx_sneha = i
    if eligible[i][0] == "S205":
        idx_arjun = i
check("tie S204 vs S205 broken by attendance", eligible[idx_sneha][2] == eligible[idx_arjun][2] and idx_arjun < idx_sneha)

# TC-08: total counts 4 eligible, 4 rejected
count_ok = 0
for a in sol.APPLICANTS:
    if sol.check_applicant(a)[0]:
        count_ok = count_ok + 1
check("4 eligible and 4 rejected out of 8", count_ok == 4 and len(sol.APPLICANTS) - count_ok == 4)

print("\nAll %d tests passed for Case Study 01" % passed)
