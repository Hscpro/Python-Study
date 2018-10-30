#!/usr/bin/env python3
import sys

indata = {}
for data in sys.argv[1:]:
    tdata = data.split(':')
    indata[tdata[0]] = tdata[1]
for key, value in indata.items():
    print("ID:{0} Name:{1}".format(key, value))
