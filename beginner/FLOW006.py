import sys

input()

for line in sys.stdin:
    digits = list(map(int, list(line.strip())))

    print(sum(digits))
