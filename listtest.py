#!/usr/bin/env python3
import sys
data1 = []
data2 = []
for indata in sys.argv[1:]:
    if len(indata) < 4:
        data1.append(indata)
    if len(indata) > 3:
        data2.append(indata)
print(data1)
print(data2)
