#!/usr/bin/env python3

import sys

gz = sys.argv[1]

try:
    gzint = int(gz)
    qisui = gzint - 3500
    sui = 0
    if qisui<1:
        sui = 0
    elif qisui<1501:
        sui = qisui*0.03-0        
    elif qisui<4501:
        sui = qisui*0.1-105
    elif qisui<9001:
        sui = qisui*0.2-555
    elif qisui<35001:
        sui = qisui*0.25-1005
    elif qisui<55001:
        sui = qisui*0.3-2755
    elif qisui<80001:
        sui = qisui*0.35-5505
    elif qisui>80000:
        sui = qisui*0.45-13505
    print("{:.2f}".format(sui,".2f"))
except:
    print("Parameter Error")

