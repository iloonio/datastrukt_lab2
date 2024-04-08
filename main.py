import sys
from class_to_file_converter import *
import matplotlib.pyplot as plt
from implemented_algorithms import *
from algorithm_benchmarking import *
from graphing import *
import numpy as np

sys.setrecursionlimit(320000)

# Generate a range of n values
n_values = np.linspace(1, 11000, 100)
# quicksort_results = generate_all_results(quicksort, "quicksort", 2000, 10001, 2000)

write_class_to_file(generate_all_results(insertion_sort, "insertionsort", 2000, 10001, 2000), "algorithm_time_results/insertionsort")

# write_class_to_file(generate_all_results(sorted, "timsort", 100000, 1000001, 100000), "algorithm_time_results/timsort")
# write_class_to_file(generate_all_results(mergesort, "mergesort", 2000, 16001, 2000), "algorithm_time_results/mergesort")
# write_class_to_file(generate_all_results(median_of_three_quicksort, "median_of_three_quicksort", 2000, 16001, 2000), "algorithm_time_results/median_of_three_quicksort")

print("done")
