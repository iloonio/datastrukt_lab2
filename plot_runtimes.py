import random
import time
from statistics import stdev
import numpy as np
from matplotlib import pyplot as plt


def measure(algorithm, int_list):
    """
    Measure the time taken for an algorithm to sort a given list.
    Perform measurements for a list of set size five times to derive the median time and standard deviation.

    :param algorithm: A sorting algorithm that takes in a list of integers and sorts them.
                 Example: sorted(), your_custom_sort_func()

    :param int_list: The list of integers to be sorted by func.
                     Should contain integers to be sorted. The list may or may not be pre-sorted.

    :return: A datapoint containing:
             - 'list_size': The number of elements in the list.
             - 'median_sort_time': The median sort time for the list.
             - 'Std_deviation': The standard deviation of sort times for the list.
    """
    return []  # Will return a datapoint with list_size, median_sort_time, and std_deviation


class SortingData:
    def __init__(self):
        self.elements = []
        self.median = []
        self.deviation = []


def generate_results(func, title, lowest_n, highest_n, n_growth):

    random_results, rising_results, falling_results, constant_results = SortingData()
    list_of_measurements = []

    print(title + " results with five measurements for each datapoint")
    print("randomized list results:")
    print("N        median          stddev          samples")
    for x in range(lowest_n, highest_n, n_growth):
        list_of_measurements.append(measure_time(func, "random", x))

    for i in list_of_measurements:
        random_results.elements.append(i.elements)
        random_results.median.append(i.median)
        random_results.deviation.append(i.deviation)

    list_of_measurements.clear()

    print("rising list results:")
    print("N        median          stddev          samples")
    for x in range(lowest_n, highest_n, n_growth):
        list_of_measurements.append(measure_time(func, "rising", x))

    for i in list_of_measurements:
        rising_results.elements.append(i.elements)
        rising_results.median.append(i.median)
        rising_results.deviation.append(i.deviation)

    list_of_measurements.clear()

    print("falling list results:")
    print("N        median          stddev          samples")
    for x in range(lowest_n, highest_n, n_growth):
        list_of_measurements.append(measure_time(func, "falling", x))

    for i in list_of_measurements:
        falling_results.elements.append(i.elements)
        falling_results.median.append(i.median)
        falling_results.deviation.append(i.deviation)

    list_of_measurements.clear()

    print("constant list results:")
    print("N        median          stddev          samples")
    for x in range(lowest_n, highest_n, n_growth):
        list_of_measurements.append(measure_time(func, "constant", x))

    for i in list_of_measurements:
        constant_results.elements.append(i.elements)
        constant_results.median.append(i.median)
        constant_results.deviation.append(i.deviation)

    # plt.plot(elements, times, label='constant list')
    # plt.errorbar(elements, times, stddevs, linestyle='none', marker='^')
    # plt.style.use('bmh')
    # plt.xlabel('elements N')
    # plt.ylabel('time taken (Seconds)')
    # plt.legend(loc=0)
    # plt.title(title)
    # plt.savefig(title)
    # plt.legend()
    # plt.show()


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

    elif array_contents == "constant":
        # Fill the list with a constant value
        array = [1.0] * size

    results = run_algorithm(func, array)  # measure_time() should return a SortingResult object
    # Containing all that good stuff we like. We're going to use this to plot a graph afterward.
    print(results.elements, results.median, results.deviation, ' 5')

    return results


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

    return SortingData(np.mean(sort_times), stdev(sort_times), len(array))


def plot_runtimes_test():
    # borrowed code from the following github repo:
    # https://gist.github.com/niftycode/917bb33be4e91a10b1fffd020f987f94
    # Stylesheets defined in Matplotlib

    # Set up runtime comparisons
    n = np.linspace(1, 6, 1000)
    labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
    big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n ** 2, n ** 3, 2 ** n]

    # Plot setup
    plt.figure(figsize=(12, 10))
    plt.ylim(0, 50)

    for i in range(len(big_o)):
        plt.plot(n, big_o[i], label=labels[i])

    plt.legend(loc=0)
    plt.ylabel('Relative Runtime')
    plt.xlabel('Input Size')
    plt.savefig('big-o-notation.png')

    plt.show()
