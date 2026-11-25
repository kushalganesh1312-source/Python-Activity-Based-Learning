# Case Study 38: ATM Menu-Driven Banking Simulation
# Name: BOPPUDI KARTHIK, Roll No: 26000451
# Uses: loops (menu), if-else, operators, lists, tuples, unpacking

OPENING_BALANCE = 10000
MIN_BALANCE = 2000
MAX_WITHDRAW = 15000
MAX_DEPOSIT = 50000


def do_deposit(balance, log, amount):
    # returns (new_balance, message, ok)
    if amount <= 0:
        return balance, "REJECTED: deposit must be positive.", False
    if amount > MAX_DEPOSIT:
        return balance, "REJECTED: deposit exceeds Rs %d limit." % MAX_DEPOSIT, False
    new_balance = balance + amount
    log.append(("DEPOSIT", amount, new_balance))
    return new_balance, "Deposited Rs %.2f. New balance Rs %.2f" % (amount, new_balance), True


def do_withdraw(balance, log, amount):
    if amount <= 0:
        return balance, "REJECTED: withdrawal must be positive.", False
    if amount % 100 != 0:
        return balance, "REJECTED: withdrawal must be multiple of Rs 100.", False
    if amount > MAX_WITHDRAW:
        return balance, "REJECTED: max withdrawal is Rs %d." % MAX_WITHDRAW, False
    if balance - amount < MIN_BALANCE:
        return balance, "REJECTED: balance will go below minimum Rs %d (current Rs %.2f)." % (MIN_BALANCE, balance), False
    new_balance = balance - amount
    log.append(("WITHDRAW", amount, new_balance))
    return new_balance, "Withdrawn Rs %.2f. New balance Rs %.2f" % (amount, new_balance), True


def show_statement(log, balance):
    print("  ---- MINI STATEMENT ----")
    if len(log) == 0:
        print("  No transactions yet.")
    for i in range(len(log)):
        kind, amt, bal = log[i]
        print("  %2d. %-8s Rs %9.2f   balance Rs %9.2f" % (i + 1, kind, amt, bal))
    print("  Current balance: Rs %.2f" % balance)


def main():
    balance = OPENING_BALANCE
    log = []
    print("=" * 54)
    print("  ATM BANKING SIMULATION (opening Rs %.2f)" % OPENING_BALANCE)
    print("=" * 54)

    while True:
        print("\n  1. Deposit        2. Withdraw")
        print("  3. Check balance  4. Mini statement")
        print("  5. Exit")
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            try:
                amount = float(input("  Deposit amount: ").strip())
                balance, msg, ok = do_deposit(balance, log, amount)
            except ValueError:
                msg = "REJECTED: enter numbers only."
            print("  " + msg)

        elif choice == "2":
            try:
                amount = float(input("  Withdraw amount: ").strip())
                balance, msg, ok = do_withdraw(balance, log, amount)
            except ValueError:
                msg = "REJECTED: enter numbers only."
            print("  " + msg)

        elif choice == "3":
            print("  Current balance: Rs %.2f" % balance)

        elif choice == "4":
            show_statement(log, balance)

        elif choice == "5":
            print("-" * 54)
            print("  Session ended: %d transaction(s), closing balance Rs %.2f" % (len(log), balance))
            print("=" * 54)
            break

        else:
            print("  REJECTED: unknown option '%s', choose 1-5." % choice)


if __name__ == "__main__":
    main()
