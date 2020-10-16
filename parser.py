from typing import TextIO
import numpy as np


class Parser:
    @staticmethod
    def parse(file: TextIO) -> dict:
        data = {}
        header_line = file.readline().split()
        values = file.readlines()

        # Read file header
        for header in header_line:
            data[header] = np.zeros(len(values))

        # Read values
        for value_index in range(len(values)):
            measures = values[value_index].split()
            for measure_index in range(len(measures)):
                current_label = header_line[measure_index]
                current_trace = data[current_label]
                current_trace[value_index] = float(measures[measure_index])

        return data
