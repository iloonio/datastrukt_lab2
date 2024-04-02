import sys
from implemented_algorithms import *
from plot_runtimes import *
import numpy as np

sys.setrecursionlimit(320000)
plt.style.use('bmh')

plot_runtimes_test()

generate_results(quicksort, "quicksort", 1000, 30001, 500)
