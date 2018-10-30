#!/usr/bin/env python3
import sys

indata = set()
for data in sys.argv[1:]:
    indata.add('{0}'.format(data))
print(indata)
