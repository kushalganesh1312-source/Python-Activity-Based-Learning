# Case Study 29: Password Policy Validation Engine
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: strings, loops, if-else, operators, boolean checks

MIN_LENGTH = 8
PROHIBITED = ["password", "123456", "admin", "welcome"]
SPECIALS = "!@#$%^&*"


def has_repeat(pw):
    # check if same character comes 3 times in a row
    run = 1
    for i in range(1, len(pw)):
        if pw[i] == pw[i - 1]:
            run = run + 1
            if run >= 3:
                return True
        else:
            run = 1
    return False


def validate_password(pw):
    errors = []

    if len(pw) < MIN_LENGTH:
        errors.append("length %d is less than minimum %d" % (len(pw), MIN_LENGTH))

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in pw:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in SPECIALS:
            has_special = True

    if has_upper == False:
        errors.append("no uppercase letter (A-Z)")
    if has_lower == False:
        errors.append("no lowercase letter (a-z)")
    if has_digit == False:
        errors.append("no digit (0-9)")
    if has_special == False:
        errors.append("no special character from %s" % SPECIALS)

    lower_pw = pw.lower()
    for word in PROHIBITED:
        if word in lower_pw:
            errors.append("contains prohibited word '%s'" % word)

    if has_repeat(pw):
        errors.append("has 3 or more same characters in a row")

    return errors


def main():
    samples = [
        "hello",
        "Pass123",
        "Campus#2026",
        "aaaBBB111!!!",
        "admin@123",
        "Karthik$99",
        "ZZZZzzzz1111!",
    ]

    print("=" * 68)
    print("  PASSWORD POLICY VALIDATION")
    print("=" * 68)
    print("Rules: length >= %d, need upper + lower + digit + special," % MIN_LENGTH)
    print("no prohibited words %s, no 3-in-a-row repeat." % PROHIBITED)
    print("-" * 68)

    passed = 0
    for pw in samples:
        errors = validate_password(pw)
        if len(errors) == 0:
            passed = passed + 1
            print("  [PASS] %-18s -> accepted" % pw)
        else:
            print("  [FAIL] %-18s -> %d problem(s)" % (pw, len(errors)))
            for e in errors:
                print("           * %s" % e)

    print("-" * 68)
    print("Result: %d out of %d passwords passed the policy." % (passed, len(samples)))


if __name__ == "__main__":
    main()
