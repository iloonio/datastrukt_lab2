import random
import time
from statistics import stdev
import numpy as np
from matplotlib import pyplot as plt


class AlgorithmResult:
    def __init__(self, rand, rising, falling, const):
        self.rand = rand
        self.rising = rising
        self.falling = falling
        self.const = const


class SortingData:
    def __init__(self):
        self.elements = []
        self.median = []
        self.deviation = []


class DataPoint:
    def __init__(self, element, median, deviation):
        self.x = element
        self.y = median
        self.y_deviation = deviation


def generate_all_results(algorithm, algorithm_title, n_min, n_max, n_growth):
    randomized_results = generate_results(algorithm, algorithm_title, "random", n_min, n_max, n_growth)
    rising_results = generate_results(algorithm, algorithm_title, "rising", n_min, n_max, n_growth)
    falling_results = generate_results(algorithm, algorithm_title, "falling", n_min, n_max, n_growth)
    const_results = generate_results(algorithm, algorithm_title, "const", n_min, n_max, n_growth)

    return AlgorithmResult(randomized_results, rising_results, falling_results, const_results)


def generate_results(func, func_title, list_type, lowest_n, highest_n, n_growth):
    resulting_data = SortingData()
    list_of_measurements = []

    # Construct the header for the output
    header = (
        f"{func_title} results with five measurements for each datapoint\n"
        f"{list_type} list results:\n"
        "N        median(ms)          stddev          samples"
    )
    print(header)

    for i in range(lowest_n, highest_n, n_growth):
        list_of_measurements.append(measure_time(func, list_type, i))

    for i in list_of_measurements:
        resulting_data.elements.append(i.x)
        resulting_data.median.append(i.y)
        resulting_data.deviation.append(i.y_deviation)

    return resulting_data


def measure_time(func, array_contents, size):
    array = [0.0] * size  # Initialize an empty list

    if array_contents == "random":
        # Generate random values
        for i in range(size):
            array[i] = random.random()

    elif array_contents == "rising":
        # Create a rising sequence
        for i in range(size):
            array[i] = i

    elif array_contents == "falling":
        # Create a falling sequence
        for i in range(size):
            array[i] = size - i - 1

    elif array_contents == "const":
        # Fill the list with a constant value
        array = [1.0] * size

    results = run_algorithm(func, array)  # measure_time() should return a SortingResult object
    # Containing all that good stuff we like. We're going to use this to plot a graph afterward.
    print(results.x, "\t", round(results.y, 10), "\t", round(results.y_deviation, 10), "\t", ' 5')

    return results


def run_algorithm(func, array):
    # measures time taken for a sorting algorithm to process an array,
    # will then append the time taken to an array.
    # returns the median of all elements inside the array
    sort_times = []
    for i in range(8):
        temp_array = list(array)
        start = time.time()
        func(temp_array)
        end = time.time()
        time_taken = (end - start) * 1000
        sort_times.append(time_taken)

    return DataPoint(len(array), np.mean(sort_times), stdev(sort_times))



