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
                       type=str,
                       help='the path to output file')

# Execute the parse_args() method
args = arg_parser.parse_args()

input_file = args.path
output_file = args.output

if not os.path.exists(input_file):
    print("Input file %s does NOT exist" % input_file)
    exit(-1)

file_stream = open(input_file, 'r', encoding='utf8')

data = Parser.parse(file_stream)

Plotter.plot(data)
