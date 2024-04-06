import sys
from class_to_file_converter import *
import matplotlib.pyplot as plt
from implemented_algorithms import *
from algorithm_benchmarking import *
from graphing import *
import numpy as np

sys.setrecursionlimit(320000)

# Generate a range of n values
n_values = np.linspace(1, 12000, 100)
# quicksort_results = generate_all_results(quicksort, "quicksort", 2000, 10001, 2000)
quicksort_results = read_class_from_file("algorithm_time_results/quicksort")

plot_series(quicksort_results.rand.elements, quicksort_results.rand.median,
            'randomized', quicksort_results.rand.deviation)
plot_k_estimate(n_values, n_log_n, 2.1e-3, 'fit n log n')
plot_k_estimate(n_values, linear, 1.7e-2, 'fit linear')
generate_graph("quicksort -- random series", "quicksort_randomized")

plot_k_estimate(n_values, quadratic, 2.1e-4, 'fit n^2')
plot_series(quicksort_results.rising.elements, quicksort_results.rising.median,
            'rising', quicksort_results.rising.deviation)
plot_series(quicksort_results.falling.elements, quicksort_results.falling.median,
            'falling', quicksort_results.falling.deviation)
plot_series(quicksort_results.const.elements, quicksort_results.const.median,
            'const', quicksort_results.const.deviation)
generate_graph("quicksort -- various series", "quicksort_various")

n_values = np.linspace(1, 11000, 100)
write_class_to_file(generate_all_results(insertion_sort, "insertionsort", 2000, 10001, 2000), "algorithm_time_results/insertionsort")
r = read_class_from_file("algorithm_time_results/insertionsort")
plot_k_estimate(n_values, quadratic, 1.7e-5, 'fit n^2')
plot_series(r.rand.elements, r.rand.deviation, 'randomized', r.rand.median)
plot_series(r.rising.elements, r.rising.deviation, 'rising', r.rising.median)
plot_series(r.falling.elements, r.falling.median, 'falling', r.falling.deviation)
plot_series(r.const.elements, r.const.median, 'const', r.const.deviation)
generate_graph("selection sort -- various series", "insertionsort_various")

print("done")
