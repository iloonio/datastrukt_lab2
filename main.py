import sys
from implemented_algorithms import *
import numpy as np

sys.setrecursionlimit(320000)  # for our sake

# We currently have this really bothersome issue: measure_time() doesn't work for insertion_sort and specifically ONLY
# insertion sort. Why??

# borrowed code from the following github repo:
# https://gist.github.com/niftycode/917bb33be4e91a10b1fffd020f987f94

# Stylesheets defined in Matplotlib
plt.style.use('bmh')

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

generate_results(sorted, "python sorted function", 20000, 100001, 20000)
print()
generate_results(mergesort, "merge sort", 20000, 100001, 20000)
print()
generate_results(median_of_three_quicksort, "median-of-three Quicksort", 200, 8001, 2000)
print()
generate_results(right_pivot_quicksort, "right-pivot quicksort", 200, 8001, 2000)
print()
generate_results(quicksort, "quicksort", 200, 8001, 2000)
print()
generate_results(bubblesort, "bubble sort", 200, 8001, 2000)
print()
generate_results(selection_sort, "selection sort", 200, 8001, 2000)
print()
generate_results(insertion_sort, "insertion sort", 200, 8001, 2000)

print("finished!")

# sorted() uses timsort, a type of hybrid algorithm
