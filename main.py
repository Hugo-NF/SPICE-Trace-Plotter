import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

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

x_label = input('Label do eixo X: ')
y_label = input('Label do eixo Y: ')

scales = input('Duas escalas? (y/n)')
right_y_label = ''
if scales == 'y':
    right_y_label = input('Label da segunda escala: ')

options = {
    'output': args.output,
    'title': args.title,
    'x_label': x_label,
    'y_label': y_label,
    'scales': scales,
    'right_y_label': right_y_label,
    'traces': {}
}

for trace in data.keys():
    if trace != 'time':
        print('Trace: %s' % trace)
        plot = input('Plot? (y/n)')
        if plot == 'y':
            options['traces'][trace] = {
                'scale': input('Segunda escala? (y/n)') if scales == 'y' else 'n',
                'label': input('Legenda'),
                'color': input('Cor'),
                'marker': input('Marcador')
            }

Plotter.plot(data, options)
