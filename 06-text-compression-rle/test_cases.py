# Test cases for Case Study 35 - Text Compression Using Character Runs
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


# TC-01: simple runs
check("aaabbbccc -> a3b3c3", sol.encode_text("aaabbbccc") == "a3b3c3")

# TC-02: single letters each get count 1
check("python -> p1y1t1h1o1n1", sol.encode_text("python") == "p1y1t1h1o1n1")

# TC-03: all same letter
check("aaaaaaaaaa -> a10", sol.encode_text("aaaaaaaaaa") == "a10")

# TC-04: empty string
check("empty -> empty", sol.encode_text("") == "")

# TC-05: single character
check("a -> a1", sol.encode_text("a") == "a1")

# TC-06: mississippi
check("mississippi encoding", sol.encode_text("mississippi") == "m1i1s2i1s2i1p2i1")

# TC-07: compression actually shorter for repetitive text
check("aaabbbccc compresses shorter", len(sol.encode_text("aaabbbccc")) < len("aaabbbccc"))

# TC-08: python becomes longer (not beneficial)
check("python becomes longer", len(sol.encode_text("python")) > len("python"))

print("\nAll %d tests passed for Case Study 35" % passed)
