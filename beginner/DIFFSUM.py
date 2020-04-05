import sys

lines = sys.stdin.readlines()
a, b = map(int, lines)

if a > b:
    print(a - b)
else:
    print(a + b)
