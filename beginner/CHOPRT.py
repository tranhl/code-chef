import sys

num_cases = int(input())
cases = sys.stdin.readlines()

for i in range(num_cases):
    a, b = map(int, cases[i].split())

    if a < b:
        print("<")
        continue

    if a > b:
        print(">")
        continue

    print("=")
