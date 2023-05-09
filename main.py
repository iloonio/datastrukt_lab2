import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from implemented_algorithms import *
import time

sys.setrecursionlimit(320000)  # for our sake

rising_array = np.arange(3200)

falling_array = rising_array[::-1]  # reversing to achieve "monotone falling"

constant_array = np.full(3200, 1)  # constant array (neither growing nor falling, nor is it randomized)

rand_quicksort_times = []
rise_quicksort_times = []
fall_quicksort_times = []
cons_quicksort_times = []

randomized_array = np.random.rand(500)
print("average time taken to sort randomized array with N500:", measure_time(quicksort, randomized_array))

randomized_array = np.random.rand(1000)
print("average time taken to sort randomized array with N1000:", measure_time(quicksort, randomized_array))

randomized_array = np.random.rand(2000)
print("average time taken to sort randomized array with N2000:", measure_time(quicksort, randomized_array))

randomized_array = np.random.rand(4000)
print("average time taken to sort randomized array with N4000:", measure_time(quicksort, randomized_array))

randomized_array = np.random.rand(8000)
print("average time taken to sort randomized array with N8000:", measure_time(quicksort, randomized_array))

print("finished")

rising_array = np.arange(500)
print("average time taken to sort rising array with N500:", measure_time(quicksort, rising_array))

rising_array = np.arange(1000)
print("average time taken to sort rising array with N1000:", measure_time(quicksort, rising_array))

rising_array = np.arange(2000)
print("average time taken to sort rising array with N2000:", measure_time(quicksort, rising_array))

rising_array = np.arange(4000)
print("average time taken to sort rising array with N4000:", measure_time(quicksort, rising_array))

rising_array = np.arange(8000)
print("average time taken to sort rising array with N8000:", measure_time(quicksort, rising_array))

print("finished")

rising_array = np.arange(500)
print("average time taken to sort falling array with N500:", measure_time(quicksort, rising_array[::-1]))

rising_array = np.arange(1000)
print("average time taken to sort falling array with N1000:", measure_time(quicksort, rising_array[::-1]))

rising_array = np.arange(2000)
print("average time taken to sort falling array with N2000:", measure_time(quicksort, rising_array[::-1]))

rising_array = np.arange(4000)
print("average time taken to sort falling array with N4000:", measure_time(quicksort, rising_array[::-1]))

rising_array = np.arange(8000)
print("average time taken to sort falling array with N8000:", measure_time(quicksort, rising_array[::-1]))
