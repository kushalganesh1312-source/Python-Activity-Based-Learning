# Test cases for Case Study 100 - Smart Campus Management Simulation
# Name: BOPPUDI KARTHIK, Roll No: 26000451
import importlib.util
import io
import os
from contextlib import redirect_stdout
from unittest import mock

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


def reset():
    sol.students.clear()
    sol.attendance.clear()
    sol.marks_records.clear()
    sol.event_regs.clear()
    sol.route_stats.clear()


def run_with_input(func, answers):
    buf = io.StringIO()
    with mock.patch("builtins.input", side_effect=answers):
        with redirect_stdout(buf):
            func()
    return buf.getvalue()


reset()

# TC-01: add valid student
run_with_input(sol.add_student, ["B1", "Karthik", "CSE"])
check("student B1 added", sol.students == [("B1", "Karthik", "CSE")])

# TC-02: duplicate roll rejected
run_with_input(sol.add_student, ["B1", "Clone", "ECE"])
check("duplicate roll rejected", len(sol.students) == 1)

# TC-03: empty roll rejected
run_with_input(sol.add_student, ["", "NoRoll", "ECE"])
check("empty roll rejected", len(sol.students) == 1)

# TC-04: attendance 18/20 = 90% eligible
out = run_with_input(sol.record_attendance, ["B1", "18", "20"])
check("attendance 90% eligible", "90.0%" in out and "ELIGIBLE" in out and sol.attendance[0] == ("B1", 18, 20))

# TC-05: attendance 13/20 = 65% not eligible
out = run_with_input(sol.record_attendance, ["B1", "13", "20"])
check("attendance 65% not eligible", "65.0%" in out and "NOT ELIGIBLE" in out)

# TC-06: present > total rejected
run_with_input(sol.record_attendance, ["B1", "25", "20"])
check("present greater than total rejected", len(sol.attendance) == 2)

# TC-07: marks recorded, avg 83.75, FIRST
out = run_with_input(sol.record_marks, ["B1", "85 78 90 82"])
check("avg 83.75 recorded", "avg=83.75" in out)
check("grade FIRST", "grade=FIRST" in out)

# TC-08: mark > 100 rejected
run_with_input(sol.record_marks, ["B1", "101 50 60 70"])
check("mark over 100 rejected", len(sol.marks_records) == 1)

# TC-09: event registration TechFest Rs 250
out = run_with_input(sol.register_event, ["B1", "1"])
check("TechFest registered Rs 250", "TechFest" in out and sol.event_regs[0][2] == 250)

# TC-10: duplicate event rejected
run_with_input(sol.register_event, ["B1", "1"])
check("duplicate event rejected", len(sol.event_regs) == 1)

# TC-11: transport R1 demand 180, cap 40, buses 4 -> served 160, unserved 20
out = run_with_input(sol.allocate_transport, ["R1", "180", "40", "4"])
check("R1 unserved 20", "unserved=20" in out)

# TC-12: summary runs and reports
out = run_with_input(sol.summary, [])
check("summary reports 1 student", "Students on roll : 1" in out)
check("summary reports revenue Rs 250", "revenue Rs 250" in out)

# TC-13: find_student
check("find_student finds B1", sol.find_student("B1")[1] == "Karthik")
check("find_student misses Z9", sol.find_student("Z9") == None)

reset()
print("\nAll %d tests passed for Case Study 100" % passed)
