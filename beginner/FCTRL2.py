import sys

input()

for line in sys.stdin:
    n = int(line.strip())
    f = 1

    for i in range(1, n + 1):
        f = f * i

    print(f)
