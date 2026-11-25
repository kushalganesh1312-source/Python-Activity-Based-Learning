# Case Study 42: Student Marks Matrix Analysis
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: nested lists, loops, if-else, operators, row/column statistics

SUBJECTS = ["Maths", "Physics", "Chemistry", "CS"]
STUDENTS = ["Karthik", "Priya", "Ravi", "Sneha"]

# rows = students, columns = subjects
MARKS = [
    [78, 82, 75, 85],
    [62, 58, 65, 60],
    [85, 80, 88, 90],
    [70, 68, 72, 74],
]

WEAK_AVG = 70.0
RISK_AVG = 60.0


def grade_of(avg):
    if avg >= 85:
        return "A (Distinction)"
    if avg >= 70:
        return "B (First Class)"
    if avg >= 55:
        return "C (Second Class)"
    return "D (Third Class)"


def main():
    print("=" * 68)
    print("  STUDENT MARKS MATRIX ANALYSIS")
    print("=" * 68)
    header = "%-9s" % "Student" + "".join("%10s" % s for s in SUBJECTS) + "%9s" % "Avg"
    print(header)
    print("-" * 68)
    for r in range(len(STUDENTS)):
        row = MARKS[r]
        total = 0
        for m in row:
            total = total + m
        avg = total / len(row)
        print("%-9s" % STUDENTS[r] + "".join("%10d" % m for m in row) + "%9.2f" % avg)
    print("-" * 68)

    print("\nRow-wise (per student):")
    best_total = -1
    best_index = -1
    for r in range(len(STUDENTS)):
        total = 0
        for m in MARKS[r]:
            total = total + m
        avg = total / len(MARKS[r])
        status = "AT RISK" if avg < RISK_AVG else "ok"
        print("  %-9s total=%3d  avg=%5.2f  grade=%-18s %s" % (STUDENTS[r], total, avg, grade_of(avg), status))
        if total > best_total:
            best_total = total
            best_index = r
    print("  -> Top performer: %s (%d marks)" % (STUDENTS[best_index], best_total))

    print("\nColumn-wise (per subject):")
    weak_list = []
    for c in range(len(SUBJECTS)):
        total = 0
        for r in range(len(STUDENTS)):
            total = total + MARKS[r][c]
        avg = total / len(STUDENTS)
        flag = ""
        if avg < WEAK_AVG:
            flag = "  << WEAK SUBJECT"
            weak_list.append(SUBJECTS[c])
        print("  %-10s average = %5.2f%s" % (SUBJECTS[c], avg, flag))

    # find highest and lowest mark with position
    high = -1
    low = 101
    hi_r = 0
    hi_c = 0
    lo_r = 0
    lo_c = 0
    for r in range(len(STUDENTS)):
        for c in range(len(SUBJECTS)):
            if MARKS[r][c] > high:
                high = MARKS[r][c]
                hi_r = r
                hi_c = c
            if MARKS[r][c] < low:
                low = MARKS[r][c]
                lo_r = r
                lo_c = c
    print("\nExtremes:")
    print("  Highest: %d (%s in %s)" % (high, STUDENTS[hi_r], SUBJECTS[hi_c]))
    print("  Lowest : %d (%s in %s)" % (low, STUDENTS[lo_r], SUBJECTS[lo_c]))
    if len(weak_list) == 0:
        print("  Weak subjects (avg < %.0f): none" % WEAK_AVG)
    else:
        joined = ""
        for i in range(len(weak_list)):
            if i > 0:
                joined = joined + ", "
            joined = joined + weak_list[i]
        print("  Weak subjects (avg < %.0f): %s" % (WEAK_AVG, joined))


if __name__ == "__main__":
    main()
