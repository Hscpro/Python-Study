#!/usr/bin/env python3

import sys
output_dict = {}


def handie_data(ins):
    ins_data = ins.split(':')
    output_dict[ins_data[0]] = ins_data[1]


def print_data(keys, dats):
    print("ID:{0} Name:{1}".format(keys, dats))


if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handie_data(arg)
    for key in output_dict:
        print_data(key, output_dict[key])
