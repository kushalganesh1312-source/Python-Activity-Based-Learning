# Test cases for Case Study 02 - Progressive Electricity Billing
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


# TC-01: 100 units only first slab: 100*4 = 400
check("energy_charge(100) = 400", sol.energy_charge(100) == 400.0)

# TC-02: 250 units: 100*4 + 150*6 = 400+900 = 1300
check("energy_charge(250) = 1300", sol.energy_charge(250) == 1300.0)

# TC-03: 400 units: 1300 + 150*8 = 1300+1200 = 2500
check("energy_charge(400) = 2500", sol.energy_charge(400) == 2500.0)

# TC-04: 450 units: 2500 + 50*10 = 3000
check("energy_charge(450) = 3000", sol.energy_charge(450) == 3000.0)

# TC-05: fixed charge and surcharge in bill
b = sol.calculate_bill(100, None)
check("fixed charge is 60", b[2] == 60.0)
check("surcharge 5% of 400 = 20", b[3] == 20.0)

# TC-06: rebate when usage decreases
b_down = sol.calculate_bill(280, 350)
check("rebate given on decrease", b_down[4] > 0)

# TC-07: no rebate when usage increases
b_up = sol.calculate_bill(350, 220)
check("no rebate on increase", b_up[4] == 0.0)

# TC-08: unusual increase check Feb->Mar: (350-220)/220 = 59% > 25%
change = (350 - 220) / 220
check("Feb to Mar is unusual increase", change > sol.UNUSUAL_LIMIT)

# TC-09: total for 100 units: 400+60+20-0 = 480
check("total for 100 units = 480", sol.calculate_bill(100, None)[5] == 480.0)

# TC-10: 5 months data
check("5 months of data present", len(sol.MONTHS) == 5)

print("\nAll %d tests passed for Case Study 02" % passed)
