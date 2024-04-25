from typing import Any
import numpy as np
import time
import random
from statistics import stdev
import matplotlib.pyplot as plt


# sorted() uses timsort, a type of hybrid algorithm


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # use a first element as our pivot (we will compare values to it)
        pivot = arr[0]
        left: list[Any] = [x for x in arr[1:] if x < pivot]
        right: list[Any] = [x for x in arr[1:] if x >= pivot]
        # Recursively apply quicksort to the left and right sub-lists,
        # and concatenate the sorted left sub-list, pivot, and sorted right sub-list in that order.
        return np.concatenate((quicksort(left), [pivot], quicksort(right)))  # we return as numpy because our arrays
        # are made with numpy and everything breaks if we don't :(


# Mergesort seems to be broken. It returns -10 on both ends of the array when It's printed out in main.py
# TODO: is this still the case?
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


def median_of_three_quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Select pivot using median-of-three strategy
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    pivot_index = np.argpartition(arr, [left, mid, right])[1]  # Index of the median value
    pivot_value = arr[pivot_index]

    # Move pivot to the rightmost position
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    # Partition the array
    i = left
    for j in range(left, right):
        if arr[j] <= pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Move pivot back to its sorted position
    arr[i], arr[right] = arr[right], arr[i]

    # Recursively sort the sub-arrays
    arr[left:i] = median_of_three_quicksort(arr[left:i])
    arr[i + 1:right + 1] = median_of_three_quicksort(arr[i + 1:right + 1])

    return arr


def right_pivot_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # use a first element as our pivot (we will compare values to it)
        pivot = len(arr) / 2
        left: list[Any] = [x for x in arr[1:] if x < pivot]
        right: list[Any] = [x for x in arr[1:] if x >= pivot]
        # Recursively apply quicksort to the left and right sub-lists,
        # and concatenate the sorted left sub-list, pivot, and sorted right sub-list in that order.
        return np.concatenate((right_pivot_quicksort(left), [pivot],
                               right_pivot_quicksort(right)))  # we return as numpy because our arrays
        # are made with numpy and everything breaks if we don't :(


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
