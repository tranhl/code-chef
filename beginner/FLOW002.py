import sys

input()

for line in sys.stdin:
    a, b = map(int, line.split())

    print(a % b)
