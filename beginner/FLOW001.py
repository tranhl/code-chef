import sys

input() # Ignore first line

for line in sys.stdin:
    a, b = map(int, line.split())

    print(a + b)
