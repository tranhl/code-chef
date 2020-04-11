import sys

# Insertion sort was initially used, but was not fast enough to satisfy time constraints.
def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i - 1
        curr, comp = arr[i], arr[j]

        # Checking if we need to sort the elements.
        if curr < comp:
            curr = arr.pop(i)  # Take out the current element.

            # Find the right insertion spot. If j == 0 then we already have the correct spot.
            while j > 0 & curr < comp:
                j -= 1
                comp = arr[j]

            arr.insert(j, curr)  # Re-insert element at correct index.

        i += 1


# Quick sort then tried out, but did not appear to be able to execute within the time
# constraints.
def quick_sort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        quick_sort(arr, low, pivotIndex - 1)
        quick_sort(arr, pivotIndex + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high - 1):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1

    swap(arr, i, high)
    return i


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# In the end using Python's built in `sort()` function worked.
def solve():
    num_cases = int(input())
    arr = list()

    for i in range(num_cases):
        arr.append(int(input()))

    arr.sort()

    for num in arr:
        print(num)


solve()
