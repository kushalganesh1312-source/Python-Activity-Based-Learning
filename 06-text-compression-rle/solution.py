# Case Study 35: Text Compression Using Character Runs (RLE)
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: strings, loops, if-else, operators, lists
# Note: input strings have letters only, so count part is not confusing


def encode_text(text):
    if text == "":
        return ""
    parts = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1
        else:
            parts.append(text[i - 1] + str(count))
            count = 1
    parts.append(text[-1] + str(count))
    result = ""
    for p in parts:
        result = result + p
    return result


def main():
    samples = [
        "aaabbbccc",
        "python",
        "aaaaaaaaaa",
        "hello",
        "zzzzzzzzzzzz",
        "mississippi",
        "",
    ]

    print("=" * 76)
    print("  TEXT COMPRESSION USING CHARACTER RUNS (RLE)")
    print("=" * 76)
    print("%-16s %5s   %-24s %5s  %s" % ("Original", "Len", "Encoded", "Len", "Result"))
    print("-" * 76)

    good = 0
    for s in samples:
        enc = encode_text(s)
        if len(enc) < len(s):
            verdict = "compressed by %d" % (len(s) - len(enc))
            good = good + 1
        elif len(enc) > len(s):
            verdict = "NOT useful (+%d)" % (len(enc) - len(s))
        else:
            verdict = "same length, not useful"
        shown_s = s
        if s == "":
            shown_s = "(empty)"
        shown_e = enc
        if enc == "":
            shown_e = "(empty)"
        print("%-16s %5d   %-24s %5d  %s" % (shown_s, len(s), shown_e, len(enc), verdict))

    print("-" * 76)
    print("Compression helped in %d out of %d samples." % (good, len(samples)))
    print("Repeated letters compress well. Short or random words become longer")
    print("because the count digits take extra space.")


if __name__ == "__main__":
    main()
