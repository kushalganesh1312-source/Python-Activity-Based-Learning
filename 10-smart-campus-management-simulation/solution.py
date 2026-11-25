# Case Study 100: Comprehensive Smart Campus Management Simulation
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: menu loop, if-else, strings, lists, tuples, unpacking, operators

students = []        # (roll, name, dept)
attendance = []      # (roll, present, total)
marks_records = []   # (roll, [m1, m2, m3, m4])
event_regs = []      # (roll, event_name, fee)
route_stats = []     # (route, demand, capacity, buses)

EVENTS = [("TechFest", 250), ("CulturalNight", 150), ("SportsMeet", 100)]


def find_student(roll):
    for s in students:
        if s[0] == roll:
            return s
    return None


def add_student():
    roll = input("  Roll no: ").strip().upper()
    if roll == "":
        print("  REJECTED: roll is required.")
        return
    if find_student(roll) != None:
        print("  REJECTED: roll %s already exists." % roll)
        return
    name = input("  Name   : ").strip()
    if name == "":
        print("  REJECTED: name is required.")
        return
    dept = input("  Department: ").strip().upper()
    students.append((roll, name, dept))
    print("  Added %s (%s, %s)." % (roll, name, dept))


def record_attendance():
    roll = input("  Roll no: ").strip().upper()
    if find_student(roll) == None:
        print("  REJECTED: unknown roll %s." % roll)
        return
    try:
        present = int(input("  Classes attended: ").strip())
        total = int(input("  Classes held     : ").strip())
    except ValueError:
        print("  REJECTED: enter numbers only.")
        return
    if total <= 0 or present < 0 or present > total:
        print("  REJECTED: invalid attendance values.")
        return
    attendance.append((roll, present, total))
    pct = present * 100.0 / total
    if pct >= 75:
        verdict = "ELIGIBLE"
    else:
        verdict = "NOT ELIGIBLE (<75%)"
    print("  %s attendance = %.1f%% -> %s" % (roll, pct, verdict))


def record_marks():
    roll = input("  Roll no: ").strip().upper()
    if find_student(roll) == None:
        print("  REJECTED: unknown roll %s." % roll)
        return
    raw = input("  Marks in 4 subjects (space separated): ").strip().split()
    if len(raw) != 4:
        print("  REJECTED: exactly 4 marks needed.")
        return
    try:
        marks = []
        for x in raw:
            marks.append(int(x))
    except ValueError:
        print("  REJECTED: marks must be integers.")
        return
    for m in marks:
        if m < 0 or m > 100:
            print("  REJECTED: marks must be within 0-100.")
            return
    marks_records.append((roll, marks))
    total = 0
    for m in marks:
        total = total + m
    avg = total / len(marks)
    if avg >= 75:
        grade = "FIRST"
    elif avg >= 60:
        grade = "SECOND"
    elif avg >= 40:
        grade = "THIRD"
    else:
        grade = "FAIL"
    print("  %s marks=%s avg=%.2f grade=%s" % (roll, marks, avg, grade))


def register_event():
    roll = input("  Roll no: ").strip().upper()
    if find_student(roll) == None:
        print("  REJECTED: unknown roll %s." % roll)
        return
    print("  Events:")
    for i in range(len(EVENTS)):
        print("    %d. %-14s fee Rs %d" % (i + 1, EVENTS[i][0], EVENTS[i][1]))
    try:
        choice = int(input("  Choice: ").strip())
    except ValueError:
        print("  REJECTED: invalid choice.")
        return
    if choice < 1 or choice > len(EVENTS):
        print("  REJECTED: choice out of range.")
        return
    event_name, fee = EVENTS[choice - 1]
    for r, ev, f in event_regs:
        if r == roll and ev == event_name:
            print("  REJECTED: already registered for %s." % event_name)
            return
    event_regs.append((roll, event_name, fee))
    print("  Registered %s for %s (Rs %d)." % (roll, event_name, fee))


def allocate_transport():
    route = input("  Route name: ").strip()
    try:
        demand = int(input("  Passenger demand: ").strip())
        capacity = int(input("  Bus capacity     : ").strip())
        buses = int(input("  Buses available  : ").strip())
    except ValueError:
        print("  REJECTED: enter numbers only.")
        return
    if demand < 0 or capacity <= 0 or buses < 0:
        print("  REJECTED: invalid transport values.")
        return
    served = buses * capacity
    if served > demand:
        served = demand
    unserved = demand - served
    route_stats.append((route, demand, capacity, buses))
    print("  %s: served=%d  unserved=%d  (buses %d x capacity %d)" % (route, served, unserved, buses, capacity))


def summary():
    print("=" * 62)
    print("  CAMPUS SUMMARY REPORT")
    print("=" * 62)
    print("  Students on roll : %d" % len(students))
    for roll, name, dept in students:
        print("     %-6s %-14s %s" % (roll, name, dept))
    print("  Attendance records: %d" % len(attendance))
    for roll, present, total in attendance:
        pct = present * 100.0 / total
        print("     %-6s %d/%d = %.1f%%" % (roll, present, total, pct))
    print("  Marks records: %d" % len(marks_records))
    for roll, marks in marks_records:
        total = 0
        for m in marks:
            total = total + m
        avg = total / len(marks)
        print("     %-6s %s avg=%.2f" % (roll, marks, avg))
    revenue = 0
    for roll, ev, fee in event_regs:
        revenue = revenue + fee
    print("  Event registrations: %d  ->  revenue Rs %d" % (len(event_regs), revenue))
    total_unserved = 0
    for route, demand, capacity, buses in route_stats:
        served = buses * capacity
        if served > demand:
            served = demand
        unserved = demand - served
        total_unserved = total_unserved + unserved
        print("     route %-6s demand=%d served=%d unserved=%d" % (route, demand, served, unserved))
    print("  Total unserved passengers: %d" % total_unserved)
    print("=" * 62)


def main():
    print("=" * 62)
    print("  SMART CAMPUS MANAGEMENT SIMULATION")
    print("=" * 62)
    while True:
        print("\n  SMART CAMPUS MENU")
        print("  1. Add student        2. Record attendance")
        print("  3. Record marks       4. Event registration")
        print("  5. Transport alloc.   6. Summary report")
        print("  0. Exit")
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            record_attendance()
        elif choice == "3":
            record_marks()
        elif choice == "4":
            register_event()
        elif choice == "5":
            allocate_transport()
        elif choice == "6":
            summary()
        elif choice == "0":
            print("  Session ended. Goodbye!")
            break
        else:
            print("  REJECTED: unknown option '%s'." % choice)


if __name__ == "__main__":
    main()
