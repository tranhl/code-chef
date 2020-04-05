import sys

num_cases, divisor = map(int, input().split())
count = 0

for line in sys.stdin:
    n = int(line)

    if n % divisor == 0:
        count += 1

print(count)
