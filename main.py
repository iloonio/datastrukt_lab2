import sys
from implemented_algorithms import *
import numpy as np

sys.setrecursionlimit(320000)  # for our sake

generate_results(insertion_sort, "insertion sort", 1000, 9001, 1000)

# We currently have this really bothersome issue: measure_time() doesnt work for insertion_sort and specifically ONLY
# insertion sort. Why??

# borrowed code from the following github repo:
# https://gist.github.com/niftycode/917bb33be4e91a10b1fffd020f987f94

# Stylesheets defined in Matplotlib
plt.style.use('bmh')

# Set up runtime comparisons
n = np.linspace(1, 5, 1000)
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n ** 2, n ** 3, 2 ** n]

# Plot setup
plt.figure(figsize=(12, 10))
plt.ylim(0, 100)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('Input Size')
plt.savefig('big-o-notation.png')

plt.show()

generate_results(sorted, "python sorted function", 10000, 50001, 10000)

generate_results(mergesort, "merge sort", 100, 1001, 100)

generate_results(median_of_three_quicksort, "median-of-three Quicksort", 100, 1001, 100)

generate_results(right_pivot_quicksort, "right-pivot quicksort", 100, 1001, 100)

generate_results(quicksort, "quicksort", 100, 1001, 100)

generate_results(bubblesort, "bubble sort", 100, 1001, 100)

generate_results(selection_sort, "selection sort", 100, 1001, 100)

generate_results(insertion_sort, "insertion sort", 100, 1001, 100)

print("finished!")

# sorted() uses timsort, a type of hybrid algorithm

"""
elements = []
times = []
stddevs = []

list_of_measurements = []
print("quicksort with randomized arrays of varying sizes")
print("N        median          stddev")

for x in range(1000, 5000, 500):
    list_of_measurements.append(measure_time(quicksort, "random", x))


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
for x in range(1000, 5000, 500):
    list_of_measurements.append(measure_time(quicksort, "rising", x))

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
for x in range(1000, 5000, 500):
    list_of_measurements.append(measure_time(quicksort, "falling", x))

for i in list_of_measurements:
    elements.append(i.elements)
    times.append(i.median)
    stddevs.append(i.deviation)

plt.plot(elements, times, label='falling list')
plt.errorbar(elements, times, stddevs, linestyle='none', marker='^')

elements.clear()
times.clear()
stddevs.clear()

list_of_measurements.clear()
for x in range(1000, 5000, 500):
    list_of_measurements.append(measure_time(quicksort, "constant", x))

for i in list_of_measurements:
    elements.append(i.elements)
    times.append(i.median)
    stddevs.append(i.deviation)

plt.plot(elements, times, label='constant list')
plt.errorbar(elements, times, stddevs, linestyle='none', marker='^')


plt.xlabel('elements N')
plt.ylabel('time taken (Seconds)')
plt.title("quicksort algorithm")
plt.legend()
plt.show()
"""
