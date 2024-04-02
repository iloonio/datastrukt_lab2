import sys
import matplotlib.pyplot as plt
from implemented_algorithms import *
from algorithm_benchmarking import *
from graphing import *
import numpy as np
sys.setrecursionlimit(320000)

k1 = 5.25e-4
# Generate a range of n values
n_values = np.linspace(1, 5000, 100)  # Adjust the range and number of points as needed
quicksort_results = generate_all_results(quicksort, "quicksort", 1000, 4001, 1000)

plot_series(quicksort_results.rand.elements, quicksort_results.rand.median,
            'randomized', quicksort_results.rand.deviation)
plot_series(quicksort_results.rising.elements, quicksort_results.rising.median,
            'rising', quicksort_results.rising.deviation)
plot_series(quicksort_results.falling.elements, quicksort_results.falling.median,
            'falling', quicksort_results.falling.deviation)
plot_series(quicksort_results.const.elements, quicksort_results.const.median,
            'const', quicksort_results.const.deviation)
plot_k_estimate(n_values, n_log_n, 5.25e-4, 'fit n log n')
plot_k_estimate(n_values, quadratic, 5.25e-5, 'fit n^2')
plot_k_estimate(n_values, log_n, 5.25e-4, 'fit log n')

generate_graph("quicksort -- various series", "quicksort_randomized")
