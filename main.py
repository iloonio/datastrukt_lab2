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
write_class_to_file(generate_all_results(insertion_sort, "insertion sort", 4000, 20001, 4000),
                    "algorithm_time_results"
                    "/insertionsort")
r = read_class_from_file("algorithm_time_results/insertionsort")
plot_series(r.rand.elements, r.rand.deviation, 'randomized', r.rand.median)
generate_graph("selection sort -- random series", "selectionsort_random")

print("done")
