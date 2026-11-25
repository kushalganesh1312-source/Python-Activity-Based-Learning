# Case Study 01: University Scholarship Allocation
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: variables, data types, operators, if-else, loops, lists, tuples, unpacking

MIN_AGGREGATE = 65.0
MIN_SUBJECT = 50
MIN_ATTENDANCE = 75.0
MAX_INCOME = 600000
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "CS"]

# each record is a tuple: (roll, name, marks list, attendance %, income)
APPLICANTS = [
    ("S201", "Karthik", [78, 82, 75, 80, 85], 90, 350000),
    ("S202", "Priya", [62, 48, 65, 60, 55], 80, 400000),
    ("S203", "Ravi", [85, 80, 88, 82, 90], 95, 280000),
    ("S204", "Sneha", [70, 68, 72, 66, 74], 82, 420000),
    ("S205", "Arjun", [70, 68, 72, 66, 74], 88, 390000),
    ("S206", "Divya", [55, 60, 52, 58, 62], 80, 300000),
    ("S207", "Manoj", [75, 70, 78, 72, 80], 70, 320000),
    ("S208", "Lakshmi", [80, 76, 84, 78, 82], 92, 650000),
]


def check_applicant(applicant):
    # unpack the tuple
    roll, name, marks, attendance, income = applicant
    total = 0
    for m in marks:
        total = total + m
    aggregate = total / len(marks)
    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("aggregate %.1f is below %.0f" % (aggregate, MIN_AGGREGATE))

    # check each subject minimum
    for i in range(len(marks)):
        if marks[i] < MIN_SUBJECT:
            reasons.append("%s mark %d is below %d" % (SUBJECTS[i], marks[i], MIN_SUBJECT))

    if attendance < MIN_ATTENDANCE:
        reasons.append("attendance %.1f%% is below %.0f%%" % (attendance, MIN_ATTENDANCE))

    if income > MAX_INCOME:
        reasons.append("income %d is above limit %d" % (income, MAX_INCOME))

    eligible = len(reasons) == 0
    return eligible, aggregate, reasons


def rank_key(record):
    # sort by aggregate high to low, then attendance high to low,
    # then income low to high, then roll number
    roll, name, aggregate, attendance, income = record
    return (-aggregate, -attendance, income, roll)


def main():
    eligible_list = []
    rejected_list = []

    for applicant in APPLICANTS:
        ok, aggregate, reasons = check_applicant(applicant)
        roll, name, marks, attendance, income = applicant
        if ok:
            eligible_list.append((roll, name, round(aggregate, 2), attendance, income))
        else:
            rejected_list.append((roll, name, reasons))

    eligible_list.sort(key=rank_key)

    print("=" * 70)
    print("  UNIVERSITY SCHOLARSHIP - ELIGIBLE APPLICANTS")
    print("=" * 70)
    print("%-6s %-10s %-10s %-11s %-10s" % ("Rank", "Roll", "Name", "Aggregate", "Attendance"))
    print("-" * 70)
    for i in range(len(eligible_list)):
        roll, name, aggregate, attendance, income = eligible_list[i]
        print("%-6d %-10s %-10s %-11.2f %-10s" % (i + 1, roll, name, aggregate, "%.1f%%" % attendance))
    print("-" * 70)

    # check for ties in aggregate
    print("\nTie check:")
    tie_found = False
    for i in range(len(eligible_list) - 1):
        if eligible_list[i][2] == eligible_list[i + 1][2]:
            tie_found = True
            a = eligible_list[i]
            b = eligible_list[i + 1]
            print("  Tie at %.2f between %s and %s -> %s has higher attendance (%.0f%% vs %.0f%%), so ranked first."
                  % (a[2], a[0], b[0], a[0], a[3], b[3]))
    if tie_found == False:
        print("  No ties found.")

    print("\nRejected applicants:")
    print("-" * 70)
    for roll, name, reasons in rejected_list:
        print("  %s (%s):" % (roll, name))
        for r in reasons:
            print("    - %s" % r)
    print("-" * 70)
    print("Total: %d eligible, %d rejected out of %d applicants."
          % (len(eligible_list), len(rejected_list), len(APPLICANTS)))


if __name__ == "__main__":
    main()
