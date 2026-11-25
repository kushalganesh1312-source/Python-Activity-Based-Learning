# Case Study 02: Progressive Electricity Billing
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: variables, operators, if-else, loops, lists, tuples, unpacking

# slabs as tuples: (upper limit, rate per unit)
SLABS = [(100, 4.0), (250, 6.0), (400, 8.0), (10000, 10.0)]
FIXED_CHARGE = 60.0
SURCHARGE_RATE = 0.05   # 5% surcharge on energy charge
REBATE_RATE = 0.10      # 10% rebate if usage falls from last month
UNUSUAL_LIMIT = 0.25    # more than 25% rise is unusual

# (month, units used)
MONTHS = [
    ("Jan", 150),
    ("Feb", 220),
    ("Mar", 350),
    ("Apr", 280),
    ("May", 240),
]


def energy_charge(units):
    # calculate slab wise charge
    charge = 0.0
    prev_limit = 0
    for limit, rate in SLABS:
        if units <= prev_limit:
            break
        if units > limit:
            slab_units = limit - prev_limit
        else:
            slab_units = units - prev_limit
        charge = charge + slab_units * rate
        prev_limit = limit
    return charge


def calculate_bill(units, prev_units):
    energy = energy_charge(units)
    surcharge = energy * SURCHARGE_RATE
    rebate = 0.0
    if prev_units != None and units < prev_units:
        rebate = energy * REBATE_RATE
    total = energy + FIXED_CHARGE + surcharge - rebate
    # return as tuple: (units, energy, fixed, surcharge, rebate, total)
    return (units, round(energy, 2), FIXED_CHARGE, round(surcharge, 2), round(rebate, 2), round(total, 2))


def main():
    bills = []
    prev = None
    for month, units in MONTHS:
        bill = calculate_bill(units, prev)
        bills.append((month, bill))
        prev = units

    print("=" * 78)
    print("  ELECTRICITY BILL STATEMENT (Progressive Tariff)")
    print("=" * 78)
    print("%-6s %7s %9s %7s %10s %8s %10s" % ("Month", "Units", "Energy", "Fixed", "Surcharge", "Rebate", "Total Rs"))
    print("-" * 78)
    for month, b in bills:
        units, energy, fixed, surcharge, rebate, total = b
        print("%-6s %7d %9.2f %7.2f %10.2f %8.2f %10.2f" % (month, units, energy, fixed, surcharge, rebate, total))
    print("-" * 78)

    print("\nMonth to month comparison:")
    print("-" * 78)
    for i in range(1, len(bills)):
        m1, b1 = bills[i - 1]
        m2, b2 = bills[i]
        change = (b2[0] - b1[0]) / b1[0]
        pct = change * 100
        flag = ""
        if change > UNUSUAL_LIMIT:
            flag = "  <-- UNUSUAL INCREASE (>25%)"
        elif change < 0:
            flag = "  (usage decreased, rebate given)"
        print("  %s -> %s : %+6.1f%%%s" % (m1, m2, pct, flag))

    # find highest and lowest bill
    highest_month = bills[0][0]
    highest_total = bills[0][1][5]
    lowest_month = bills[0][0]
    lowest_total = bills[0][1][5]
    for month, b in bills:
        if b[5] > highest_total:
            highest_total = b[5]
            highest_month = month
        if b[5] < lowest_total:
            lowest_total = b[5]
            lowest_month = month
    print("\nHighest bill: %s Rs %.2f" % (highest_month, highest_total))
    print("Lowest bill : %s Rs %.2f" % (lowest_month, lowest_total))


if __name__ == "__main__":
    main()
