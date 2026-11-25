# Case Study 64: Tuple-Based Course Registration Validation
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: tuples, nested tuples, unpacking, lists, loops, if-else

MAX_COURSES = 4
# prerequisite: course -> needed course
PREREQ = [("CS201", "CS101"), ("CS301", "CS201")]
# these two cannot be taken together
EXCLUSIVE = [("PHY101", "PHY102")]
KNOWN = ["CS101", "CS201", "CS301", "MATH101", "PHY101", "PHY102", "ENG101"]

# each record: (roll, name, ((code, title), ...))
REGISTRATIONS = [
    ("R01", "Karthik", (
        ("CS101", "Intro Programming"),
        ("MATH101", "Calculus"),
        ("PHY101", "Physics I"),
    )),
    ("R02", "Priya", (
        ("CS101", "Intro Programming"),
        ("CS101", "Intro Programming"),
        ("CS201", "Data Structures"),
    )),
    ("R03", "Ravi", (
        ("CS201", "Data Structures"),
        ("MATH101", "Calculus"),
    )),
    ("R04", "Sneha", (
        ("CS101", "Intro Programming"),
        ("PHY101", "Physics I"),
        ("PHY102", "Physics II"),
        ("MATH101", "Calculus"),
        ("ENG101", "Technical English"),
    )),
    ("R05", "Arjun", (
        ("CS101", "Intro Programming"),
        ("CS201", "Data Structures"),
        ("MATH101", "Calculus"),
        ("ENG101", "Technical English"),
    )),
    ("R06", "Divya", (
        ("CS301", "Algorithms"),
        ("MATH101", "Calculus"),
    )),
]


def find_prereq(course):
    for c, need in PREREQ:
        if c == course:
            return need
    return None


def validate(student):
    roll, name, courses = student
    codes = []
    for code, title in courses:
        codes.append(code)

    problems = []

    # duplicate check
    for c in codes:
        if codes.count(c) > 1:
            msg = "duplicate '%s'" % c
            if msg not in problems:
                problems.append(msg)

    # too many courses
    if len(courses) > MAX_COURSES:
        problems.append("registered for %d courses (max %d)" % (len(courses), MAX_COURSES))

    # prerequisite check
    for c in codes:
        need = find_prereq(c)
        if need != None and need not in codes:
            msg = "missing prerequisite %s for %s" % (need, c)
            if msg not in problems:
                problems.append(msg)

    # exclusive pair check
    for a, b in EXCLUSIVE:
        if a in codes and b in codes:
            problems.append("exclusive pair %s + %s together" % (a, b))

    # unknown code check
    for c in codes:
        if c not in KNOWN:
            problems.append("unknown course code '%s'" % c)

    return problems


def main():
    print("=" * 72)
    print("  COURSE REGISTRATION VALIDATION (Tuples)")
    print("=" * 72)
    print("Rules: max %d courses, no duplicates, prerequisites needed," % MAX_COURSES)
    print("exclusive pair not together, only known codes allowed.")
    print("-" * 72)

    invalid_count = 0
    for student in REGISTRATIONS:
        roll, name, courses = student
        codes = []
        for code, title in courses:
            codes.append(code)
        problems = validate(student)
        if len(problems) == 0:
            status = "VALID"
        else:
            status = "INVALID"
            invalid_count = invalid_count + 1
        joined = ""
        for i in range(len(codes)):
            if i > 0:
                joined = joined + ", "
            joined = joined + codes[i]
        print("  %s (%s) - %d course(s): %s" % (roll, name, len(courses), joined))
        print("      -> %s" % status)
        for p in problems:
            print("         * %s" % p)

    print("-" * 72)
    valid_count = len(REGISTRATIONS) - invalid_count
    print("Summary: %d valid, %d invalid student(s)." % (valid_count, invalid_count))
    print("Invalid students:")
    for student in REGISTRATIONS:
        if len(validate(student)) > 0:
            roll, name, courses = student
            print("   - %s %s" % (roll, name))


if __name__ == "__main__":
    main()
