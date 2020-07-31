#!/usr/bin/env python3
import fileinput

# fileinput allows script to take in data from number of sources
# piping, file, filename passed in, or command line
with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

# print output from several files at once
with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')