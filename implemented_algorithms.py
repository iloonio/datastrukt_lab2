from typing import Any
import numpy as np
import time
from statistics import stdev
import matplotlib as plt


class SortingResult:  # this could've been a struct, but we can't have those in python...
    def __init__(self, median, deviation, elements):
        self.median = median
        self.deviation = deviation
        self.elements = elements


def run_algorithm(func, array):
    # measures time taken for a sorting algorithm to process an array,
    # will then append the time taken to an array.
    # returns the median of all elements inside the array
    sort_times = []
    for i in range(5):
        start = time.time()
        func(array)
        end = time.time()
        time_taken = end - start
        sort_times.append(time_taken)

    return SortingResult(np.median(sort_times), stdev(sort_times), len(array))


def measure_time(func, array_type, size):
    array = np.random.rand(size)  # default case

    match array_type:
        case "random":
            array = np.random.rand(size)

        case "rising":
            array = np.arange(size)

        case "falling":
            array = np.arange(size)[::-1]

        case "constant":
            array = np.full(size, 1)

    results = run_algorithm(func, array)  # measure_time() should return a SortingResult object
    # Containing all that good stuff we like. We're going to use this to plot a graph afterward.
    print(results.elements, results.median, results.deviation)

    return results


def plot_graph(sorting_result):
    # this is going to take in an array holding multiple sorting results, and then they will be plotted to reveal a
    # graph.
    plt.xlabel('elements N')
    plt.ylabel('time taken')
    plt.plot(sorting_result.elements, sorting_result.median)
    plt.show()


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
