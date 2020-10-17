import os
import argparse

from parser import Parser
from plotter import Plotter

# Create the parser
arg_parser = argparse.ArgumentParser(description='Plot charts from SPICE text results')

# Add the arguments
arg_parser.add_argument('path',
                        metavar='path',
                        type=str,
                        help='the path to SPICE text results')

arg_parser.add_argument('output',
                        metavar='output',
                        default='output.png',
                        type=str,
                        help='the path to output file')

arg_parser.add_argument('title',
                        metavar='title',
                        type=str,
                        help='chart title')

# Execute the parse_args() method
args = arg_parser.parse_args()

input_file = args.path

if not os.path.exists(input_file):
    print("Input file %s does NOT exist" % input_file)
    exit(-1)

file_stream = open(input_file, 'r', encoding='utf8')

data = Parser.parse(file_stream)

options = {
    'output': 'docs/boost.png',
    'title': 'Conversor Boost',
    'x_label': 'Tempo (s)',
    'x_transform': 0.001,
    'y_label': 'Tensão (V)',
    'y_transform': 1,
    'scales': 'y',
    'right_y_label': 'Corrente (mA)',
    'right_y_transform': 1000,
    'traces': {
        'V(vin)': {
            'scale': 'n',
            'label': 'Vin',
            'color': 'blue',
            'marker': ''
        },
        'V(vout)': {
            'scale': 'n',
            'label': 'Vout',
            'color': 'green',
            'marker': ''
        },
        'I(R1)': {
            'scale': 'y',
            'label': 'I(R1)',
            'color': 'red',
            'marker': ''
        }
    }
}

Plotter.plot(data, options)
