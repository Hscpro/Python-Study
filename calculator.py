"""
测试：101:3500 203:5000 309:15000 207:6000
挑战：https://www.shiyanlou.com/courses/1140/labs/7269/document
"""

#!/usr/bin/env python3
import sys


def Rins():
    ID_Dat = []
    NA_Dat = []
    try:
        for ins in sys.argv[1:]:
            tmp_in = ins.split(':')
            ID_Dat.append(tmp_in[0])
            NA_Dat.append(int(tmp_in[1]))
        return ID_Dat, NA_Dat
    except:
        print("Parameter Error")


def Count(dat):
    try:
        bind = len(dat)
        bins = 0
        while bins < bind:
            if dat[bins] <= 0:
                return dat[bins]
            else:
                sefat = dat[bins] * 0.165
                ifdat = dat[bins] - (3500 + sefat)
                if ifdat < 0:
                    dat[bins] = dat[bins]
                elif ifdat <= 1500:
                    dat[bins] -= ifdat * 0.03 - 0
                elif ifdat <= 4500:
                    dat[bins] -= ifdat * 0.1 - 105
                elif ifdat <= 9000:
                    dat[bins] -= ifdat * 0.2 - 555
                elif ifdat <= 35000:
                    dat[bins] -= ifdat * 0.25 - 1005
                elif ifdat <= 55000:
                    dat[bins] -= ifdat * 0.3 - 2755
                elif ifdat <= 80000:
                    dat[bins] -= ifdat * 0.35 - 5505
                else:
                    dat[bins] -= ifdat * 0.45 - 13505
                dat[bins] -= sefat
            bins += 1
        return dat
    except:
        print("Parameter Error")


def Display(iddat, nadat):
    bind = len(iddat)
    bins = 0
    while bins < bind:
        print("{0}:{1:.2f}".format(iddat[bins], nadat[bins]))
        bins += 1


if __name__ == '__main__':
    try:
        Indata = Rins()
        Codata = Count(Indata[1])
        Display(Indata[0], Codata)
    except:
        print("Parameter Error")
