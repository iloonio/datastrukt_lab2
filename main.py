import sys
from class_to_file_converter import *
import matplotlib.pyplot as plt
from implemented_algorithms import *
from algorithm_benchmarking import *
from graphing import *
import numpy as np

sys.setrecursionlimit(320000)

# Generate a range of n values

# quicksort_results = generate_all_results(quicksort, "quicksort", 2000, 10001, 2000) write_class_to_file(
# generate_all_results(insertion_sort, "insertionsort", 2000, 10001, 2000), "algorithm_time_results/insertionsort")
# write_class_to_file(generate_all_results(sorted, "timsort", 100000, 1000001, 100000),
# "algorithm_time_results/timsort") write_class_to_file(generate_all_results(mergesort, "mergesort", 2000, 16001,
# 2000), "algorithm_time_results/mergesort") write_class_to_file(generate_all_results(median_of_three_quicksort,
# "median_of_three_quicksort", 2000, 16001, 2000), "algorithm_time_results/median_of_three_quicksort")

time_results = ["bubblesort", "insertionsort", "median_of_three_quicksort", "mergesort", "quicksort",
                "right_pivot_quicksort", "selectionsort", "timsort"]

# plot_k_estimate(n_values, quadratic, 4.9e-5, "n^2 fit for rising & const series")
# plot_k_estimate(n_values, quadratic, 8.2e-5, "n^2 fit for random series")
# plot_k_estimate(n_values, quadratic, 1.05e-4, "n^2 fit for falling series")
# plot_all_from_file("bubblesort")


# plot_series(fileInput.rand.elements, fileInput.rand.median, "random series", fileInput.rand.deviation)
# plot_k_estimate(n_values, quadratic, 3.2e-5, "n^2 fit")


# plot_series(fileInput.rising.elements, fileInput.rising.median, "rising series", fileInput.rising.deviation)
# plot_series(fileInput.const.elements, fileInput.const.median, "const series", fileInput.const.deviation)
# plot_k_estimate(n_values, linear, 1.75e-4, "linear fit")

# plot_series(fileInput.falling.elements, fileInput.falling.median, "falling series", fileInput.falling.deviation)
# plot_k_estimate(n_values, quadratic, 6.5e-5, "n^2 fit")

# plot_series(fileInput.const.elements, fileInput.const.median, "const series", fileInput.const.deviation)
# plot_k_estimate(n_values, quadratic, 1.3e-4, "n^2 fit")

# plot_series(fileInput.rand.elements, fileInput.rand.median, "random series", fileInput.rand.deviation)
# plot_series(fileInput.falling.elements, fileInput.falling.median, "falling series", fileInput.falling.deviation)
# plot_k_estimate(n_values, n_log_n, 3.2e-4, "n log n fit falling series")
# plot_k_estimate(n_values, n_log_n, 3.8e-4, "n log n fit random series")

# plot_series(fileInput.rising.elements, fileInput.rising.median, "rising series", fileInput.rising.deviation)
# plot_series(fileInput.const.elements, fileInput.const.median, "const series", fileInput.const.deviation)
# plot_k_estimate(n_values, linear, 2.55e-3, "n linear fit")

# plot_series(fileInput.const.elements, fileInput.const.median, "const series", fileInput.const.deviation)
# plot_series(fileInput.falling.elements, fileInput.falling.median, "falling series", fileInput.falling.deviation)
# plot_series(fileInput.rising.elements, fileInput.rising.median, "rising series", fileInput.rising.deviation)
# plot_k_estimate(n_values, quadratic, 2.1e-4, "n^2 fit")

# plot_series(fileInput.rand.elements, fileInput.rand.median, "random series", fileInput.rand.deviation)

# write_class_to_file(generate_all_results(sorted, "timsort", 1000000, 10000000, 1000000),
#                    "algorithm_time_results/timsort")



# plot_series(fileInput.rand.elements, fileInput.rand.median, "random series", fileInput.rand.deviation)
# plot_series(fileInput.falling.elements, fileInput.falling.median, "falling series", fileInput.falling.deviation)
# plot_series(fileInput.rising.elements, fileInput.rising.median, "rising series", fileInput.rising.deviation)
# plot_series(fileInput.const.elements, fileInput.const.median, "const series", fileInput.const.deviation)
# plot_k_estimate(n_values, linear, 5.0e-6, " linear n fit const series")
# plot_k_estimate(n_values, n_log_n, 1.74e-5, "n log n fit")

fileInput = read_class_from_file("algorithm_time_results/median_of_three_quicksort")
n_values = np.linspace(1, 18000, 100)

plot_series(fileInput.rising.elements, fileInput.rising.median, "rising series", fileInput.rising.deviation)
plot_series(fileInput.falling.elements, fileInput.falling.median, "falling series", fileInput.falling.deviation)
plot_k_estimate(n_values, quadratic, 3.1e-5, "n^2 fit falling")
plot_k_estimate(n_values, quadratic, 4.6e-5, "n^2 fit rising")

generate_graph("m3 quicksort - rising & falling series", "median_of_three_quicksort_rising_falling")

print("done")
