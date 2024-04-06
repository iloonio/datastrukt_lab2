# TODO: create a method that converts data from benchmarking into a file, and vice-versa
from collections import defaultdict

from algorithm_benchmarking import *


def write_class_to_file(obj: AlgorithmResult, file):
    with open(file, 'w') as file:
        file.write(f"random series \n elements, median, deviation \n")
        for i in range(len(obj.rand.elements)):
            file.write(f"{obj.rand.elements[i]}, {obj.rand.median[i]}, {obj.rand.deviation[i]} \n")
        file.write("\n")

        file.write(f"rising series \n elements, median, deviation \n")
        for i in range(len(obj.rising.elements)):
            file.write(f"{obj.rising.elements[i]}, {obj.rising.median[i]}, {obj.rising.deviation[i]} \n")
        file.write("\n")

        file.write(f"falling series \n elements, median, deviation \n")
        for i in range(len(obj.falling.elements)):
            file.write(f"{obj.falling.elements[i]}, {obj.falling.median[i]}, {obj.falling.deviation[i]} \n")
        file.write("\n")

        file.write(f"const series \n elements, median, deviation \n")
        for i in range(len(obj.const.elements)):
            file.write(f"{obj.const.elements[i]}, {obj.const.median[i]}, {obj.const.deviation[i]} \n")


def read_class_from_file(file: str) -> AlgorithmResult:
    result_dict = defaultdict(SortingData)
    current_series = None

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line in ['random series', 'rising series', 'falling series', 'const series']:
                current_series = line
            elif line == 'elements, median, deviation':
                next(f)  # Skip header line
                data_line = next(f).strip()
                data = [float(entry) for entry in data_line.split(',')]
                setattr(result_dict[current_series], 'elements', data[0])
                setattr(result_dict[current_series], 'median', data[1])
                setattr(result_dict[current_series], 'deviation', data[2])
                next(f)  # Skip extra newline
            else:
                continue

    return AlgorithmResult(result_dict['random series'], result_dict['rising series'],
                           result_dict['falling series'], result_dict['const series'])




