import sys

num_cases = int(input())
years = list(map(int, sys.stdin.readlines()))
valid_years = [2010, 2015, 2016, 2017, 2019]

for i in range(num_cases):
    year = years[i]

    if valid_years.count(year) > 0:
        print("HOSTED")
    else:
        print("NOT HOSTED")
