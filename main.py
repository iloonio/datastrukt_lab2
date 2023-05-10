import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from implemented_algorithms import *
import time

sys.setrecursionlimit(320000)  # for our sake
print("quicksort with randomized arrays of varying sizes")
print("N        median          stddev")
measure_time(quicksort, "random", 500)
measure_time(quicksort, "random", 1000)
measure_time(quicksort, "random", 2000)
measure_time(quicksort, "random", 4000)
measure_time(quicksort, "random", 8000)

print("quicksort with constant values in an array of varying sizes")
print("N        median          stddev")
measure_time(quicksort, "constant", 500)
measure_time(quicksort, "constant", 1000)
measure_time(quicksort, "constant", 2000)
measure_time(quicksort, "constant", 4000)
measure_time(quicksort, "constant", 8000)

print("quicksort with rising array of varying sizes")
print("N        median          stddev")
measure_time(quicksort, "rising", 500)
measure_time(quicksort, "rising", 1000)
measure_time(quicksort, "rising", 2000)
measure_time(quicksort, "rising", 4000)
measure_time(quicksort, "rising", 8000)

