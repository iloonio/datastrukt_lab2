import sys

import matplotlib.pyplot as plt
from implemented_algorithms import *
from algorithm_benchmarking import *
import numpy as np

sys.setrecursionlimit(320000)
plt.style.use('bmh')

k1 = 5.25e-4


def quadratic(n):
    return n * n


def n_log_n(n):
    return n * np.log(n)


def log_n(n):
    return np.log(n)


def linear(n):
    return n


# Generate a range of n values
n_values = np.linspace(1, 10000, 100)  # Adjust the range and number of points as needed

plt.plot(n_values, k1 * n_log_n(n_values), label='f(n) = k * n * log(n)')
plt.plot(n_values, k1 * log_n(n_values), label='g(n) = k * log(n)')
plt.plot(n_values, k1 * linear(n_values), label='h(n) = k * n')
plt.plot(n_values, k1 * quadratic(n_values), label='j(n) = k * n^2')

quicksort_results = generate_all_results(quicksort, "quicksort", 1000, 8001, 1000)

plt.plot(quicksort_results.rand.elements, quicksort_results.rand.median, label='quicksort -- '
                                                                               'random series')
plt.errorbar(quicksort_results.rand.elements, quicksort_results.rand.median,
             quicksort_results.rand.deviation, linestyle='none', marker='^')
plt.style.use('bmh')
plt.xlabel('elements (n)')
plt.ylabel('median time (ms)')
plt.legend(loc=0)
plt.title("quicksort on a randomized list")
plt.savefig("quicksort_random")
plt.grid(True)
plt.legend()
plt.show()

# plot_runtimes_test()
