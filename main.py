import os
import json

from parser import Parser
from plotter import Plotter

try:
    with open('settings.json', 'r') as settings_file:
        options = json.load(settings_file)
        print(options)
except FileNotFoundError:
    print('Missing configuration file: settings.json. Nothing to do...')
    exit(-1)

if not os.path.exists(options['input']):
    print("Input file %s does NOT exist" % options['input'])
    exit(-1)

file_stream = open(options['input'], 'r', encoding='utf8')

data = Parser.parse(file_stream)

Plotter.plot(data, options)
