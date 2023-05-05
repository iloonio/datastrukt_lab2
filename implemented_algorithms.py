from typing import Any
import numpy as np
import time


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # use first element as our pivot (we will compare values to it)
        pivot = arr[0]
        left: list[Any] = [x for x in arr[1:] if x < pivot]
        right: list[Any] = [x for x in arr[1:] if x >= pivot]
        # Recursively apply quicksort to the left and right sub-lists,
        # and concatenate the sorted left sub-list, pivot, and sorted right sub-list in that order.
        return np.concatenate((quicksort(left), [pivot], quicksort(right)))  # we return as numpy because our arrays
        # are made with numpy and everything breaks if we don't :(


# mergesort seems to be broken. It returns -10 on both ends of the array when its printed out in main.py
def mergesort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        left = arr[:mid]
        right = arr[mid:]

        # Sorting the halves
        mergesort(left)
        mergesort(right)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    return arr


def bubblesort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def measure_time(func, array):
    print("size of array: ", len(array))
    start = time.time()
    func(array)
    end = time.time()
    return end - start
