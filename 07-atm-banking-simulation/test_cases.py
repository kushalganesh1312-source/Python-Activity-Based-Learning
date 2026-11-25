# Test cases for Case Study 38 - ATM Menu-Driven Banking Simulation
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


# TC-01: valid deposit
log = []
new_bal, msg, ok = sol.do_deposit(10000, log, 5000)
check("deposit 5000 accepted", ok == True and new_bal == 15000 and len(log) == 1)

# TC-02: negative deposit rejected
log = []
new_bal, msg, ok = sol.do_deposit(10000, log, -500)
check("negative deposit rejected", ok == False and new_bal == 10000)

# TC-03: deposit over limit rejected
log = []
new_bal, msg, ok = sol.do_deposit(10000, log, 60000)
check("deposit over 50000 rejected", ok == False)

# TC-04: valid withdrawal
log = []
new_bal, msg, ok = sol.do_withdraw(12000, log, 3000)
check("withdraw 3000 accepted", ok == True and new_bal == 9000)

# TC-05: withdrawal not multiple of 100
log = []
new_bal, msg, ok = sol.do_withdraw(10000, log, 250)
check("withdraw 250 rejected, not multiple of 100", ok == False and "multiple" in msg)

# TC-06: withdrawal over max
log = []
new_bal, msg, ok = sol.do_withdraw(50000, log, 20000)
check("withdraw over 15000 rejected", ok == False and "max" in msg.lower())

# TC-07: withdrawal below minimum balance
log = []
new_bal, msg, ok = sol.do_withdraw(4000, log, 3000)
check("withdraw below min balance rejected", ok == False and "minimum" in msg)

# TC-08: withdrawal exactly to minimum balance allowed (4000-2000=2000)
log = []
new_bal, msg, ok = sol.do_withdraw(4000, log, 2000)
check("withdraw to exactly 2000 allowed", ok == True and new_bal == 2000)

# TC-09: non-numeric input handling
try:
    amount = float("abc")
    ok = True
except ValueError:
    ok = False
check("non-numeric input caught", ok == False)

# TC-10: log keeps running balance
log = []
bal = 10000
bal, _, _ = sol.do_deposit(bal, log, 1000)
bal, _, _ = sol.do_withdraw(bal, log, 500)
bal, _, _ = sol.do_deposit(bal, log, 200)
check("3 log entries, second balance 10500", len(log) == 3 and log[1][2] == 10500)

print("\nAll %d tests passed for Case Study 38" % passed)
