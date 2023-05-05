import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from implemented_algorithms import *
import time

sys.setrecursionlimit(320000)  # for our sake

rising_array = np.arange(3200)

falling_array = rising_array[::-1]  # reversing to achieve "monotone falling"

randomized_array = np.random.rand(3200)

constant_array = np.full(3200, 1)  # constant array (neither growing nor falling, nor is it randomized)

time_taken = measure_time(quicksort, randomized_array)
print("time taken to sort randomized array:", time_taken)

time_taken = measure_time(quicksort, rising_array)
print("Time taken to sort rising array:", time_taken)

time_taken = measure_time(quicksort, constant_array)
print("time taken to sort constant array:", time_taken)


