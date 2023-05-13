from typing import Any
import numpy as np
import time
from statistics import stdev
import matplotlib.pyplot as plt


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
    for i in range(10):
        start = time.time()
        func(array)
        end = time.time()
        time_taken = end - start
        sort_times.append(time_taken)

    return SortingResult(np.mean(sort_times), stdev(sort_times), len(array))


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
    print(results.elements, results.median, results.deviation, ' 10')

    return results


def generate_results(func, title, lowest_N, highest_N, N_growth):
    elements = []
    times = []
    stddevs = []
    list_of_measurements = []
    print(title + " results with five measurements for each datapoint")
    print("randomized list results:")
    print("N        median          stddev          samples")
    for x in range(lowest_N, highest_N, N_growth):
        list_of_measurements.append(measure_time(func, "random", x))

    for i in list_of_measurements:
        elements.append(i.elements)
        times.append(i.median)
        stddevs.append(i.deviation)

    plt.plot(elements, times, label="randomized list")
    plt.errorbar(elements, times, stddevs, linestyle='none', marker='^')

    elements.clear()
    times.clear()
    stddevs.clear()
    list_of_measurements.clear()

    print("rising list results:")
    print("N        median          stddev          samples")
    for x in range(lowest_N, highest_N, N_growth):
        list_of_measurements.append(measure_time(func, "rising", x))

    for i in list_of_measurements:
        elements.append(i.elements)
        times.append(i.median)
        stddevs.append(i.deviation)

    plt.plot(elements, times, label='rising list')
    plt.errorbar(elements, times, stddevs, linestyle='none', marker='^')

    elements.clear()
    times.clear()
    stddevs.clear()
    list_of_measurements.clear()

    print("falling list results:")
    print("N        median          stddev          samples")
    for x in range(lowest_N, highest_N, N_growth):
        list_of_measurements.append(measure_time(func, "falling", x))

    for i in list_of_measurements:
        elements.append(i.elements)
        times.append(i.median)
        stddevs.append(i.deviation)

    plt.plot(elements, times, label='falling list')
    plt.errorbar(elements, times, stddevs, linestyle='none', marker='^')

    elements.clear()
    times.clear()
    stddevs.clear()

    print("constant list results:")
    print("N        median          stddev          samples")
    list_of_measurements.clear()
    for x in range(lowest_N, highest_N, N_growth):
        list_of_measurements.append(measure_time(func, "constant", x))

    for i in list_of_measurements:
        elements.append(i.elements)
        times.append(i.median)
        stddevs.append(i.deviation)

    plt.plot(elements, times, label='constant list')
    plt.errorbar(elements, times, stddevs, linestyle='none', marker='^')
    plt.style.use('bmh')
    plt.xlabel('elements N')
    plt.ylabel('time taken (Seconds)')
    plt.legend(loc=0)
    plt.title(title)
    plt.savefig(title)
    plt.legend()
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
