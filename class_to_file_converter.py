# TODO: create a method that converts data from benchmarking into a file, and vice-versa
from collections import defaultdict

from algorithm_benchmarking import *


def write_class_to_file(obj: AlgorithmResult, file):
    with open(file, 'w') as file:
        for series_name, series_data in [('random series', obj.rand), ('rising series', obj.rising),
                                         ('falling series', obj.falling), ('const series', obj.const)]:
            file.write(f"{series_name}\n")
            for i in range(len(series_data.elements)):
                file.write(f"{series_data.elements[i]}, {series_data.median[i]}, {series_data.deviation[i]}\n")
            file.write("\n")


def read_class_from_file(file: str) -> AlgorithmResult:
    result_dict = defaultdict(SortingData)
    current_series = None

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line in ['random series', 'rising series', 'falling series', 'const series']:
                current_series = line
            elif line:  # Only process non-empty lines
                data = [float(entry) for entry in line.split(',')]
                result_dict[current_series].elements.append(data[0])
                result_dict[current_series].median.append(data[1])
                result_dict[current_series].deviation.append(data[2])

    return AlgorithmResult(result_dict['random series'], result_dict['rising series'],
                           result_dict['falling series'], result_dict['const series'])










