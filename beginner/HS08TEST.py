amount, balance = map(float, input().split())
output = "%.2f"


def solve():
    if amount % 5 != 0:
        print(output % balance)
        return

    if amount + 0.5 > balance:
        print(output % balance)
        return

    print(output % (balance - amount - 0.5))


solve()
