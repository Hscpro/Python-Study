#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv, sys

# 读取参数
def RinsFileAs():
    cfg_Dat = None
    csv_Dat = None
    out_Dat = None
    if len(sys.argv) > 6:
        count = 1
        while count <= 6:
            if sys.argv[count] == '-c':
                count += 1
                cfg_Dat = sys.argv[count]
            elif sys.argv[count] == '-d':
                count += 1
                csv_Dat = sys.argv[count]
            elif sys.argv[count] == '-o':
                count += 1
                out_Dat = sys.argv[count]
            count += 1
    if cfg_Dat != None and csv_Dat != None and out_Dat != None:
        return cfg_Dat, csv_Dat, out_Dat
    else:
        return 1

# 读取配置文件
def RinsCfg(FileAs):
    CfgDat = {}
    with open(FileAs) as FileDat:
        for ListDat in FileDat:
            ListDatTmp = ListDat.split()
            CfgDat[ListDatTmp[0]] = float(ListDatTmp[2])
    return CfgDat

# 读取员工数据文件
def RinsCsv(FileAs):
    __UserID = []
    __UserDa = []
    with open(FileAs) as FileDat:
        UserDat = list(csv.reader(FileDat))
    for UserDatTmp in UserDat:
        #工号
        __UserID.append(UserDatTmp[0])
        #工资
        __UserDa.append(float(UserDatTmp[1]))
    return __UserID, __UserDa

# 计算五险一金
def CountSafe(Safe, UserDat):
    __UserSafeDat = []
    for UserDatTmp in UserDat:
        if UserDatTmp < Safe['JiShuL']:
            __UserSafeDat.append(Safe['JiShuL'] * (Safe['YangLao'] + Safe['YiLiao'] + Safe['ShiYe'] + Safe['GongShang'] + Safe['ShengYu'] + Safe['GongJiJin']))
        elif UserDatTmp > Safe['JiShuH']:
            __UserSafeDat.append(Safe['JiShuH'] * (Safe['YangLao'] + Safe['YiLiao'] + Safe['ShiYe'] + Safe['GongShang'] + Safe['ShengYu'] + Safe['GongJiJin']))
        else:
            __UserSafeDat.append(UserDatTmp * (Safe['YangLao'] + Safe['YiLiao'] + Safe['ShiYe'] + Safe['GongShang'] + Safe['ShengYu'] + Safe['GongJiJin']))
    return __UserSafeDat

# 计算应缴税
def CountTax(Safe, User):
    __UserTaxDat = []
    for (UserTmp, SafeTmp) in zip(User, Safe):
        UserTaxTmp = UserTmp - (SafeTmp + 3500)
        if UserTaxTmp <= 0:
            __UserTaxDat.append(0)
        elif UserTaxTmp <= 1500:
            __UserTaxDat.append(UserTaxTmp * 0.03 - 0)
        elif UserTaxTmp <= 4500:
            __UserTaxDat.append(UserTaxTmp * 0.10 - 105)
        elif UserTaxTmp <= 9000:
            __UserTaxDat.append(UserTaxTmp * 0.20 - 555)
        elif UserTaxTmp <= 35000:
            __UserTaxDat.append(UserTaxTmp * 0.25 - 1005)
        elif UserTaxTmp <= 55000:
            __UserTaxDat.append(UserTaxTmp * 0.30 - 2755)
        elif UserTaxTmp <= 80000:
            __UserTaxDat.append(UserTaxTmp * 0.35 - 5505)
        else:
            __UserTaxDat.append(UserTaxTmp * 0.45 - 13505)
    return __UserTaxDat

# 输出CSV文件
def OutData(FileAs, UserID, UserDA, Safe, Tax):
    __CsvData = []
    # 每员工占用一个 tuple
    for (UserIDTmp, UserDATmp, SafeTmp, TaxTmp) in zip(UserID, UserDA, Safe, Tax):
        #工号,税前工资,社保金额,个税金额,税后工资
        __CsvData.append([
            UserIDTmp, 
            UserDATmp, 
            "{:.2f}".format(SafeTmp), 
            "{:.2f}".format(TaxTmp), 
            "{:.2f}".format(UserDATmp - (SafeTmp + TaxTmp))
        ])
    #将数据输出到csv文件
    with open(FileAs, 'w', encoding='utf8', newline='') as FileDat:
        csv.writer(FileDat).writerows(__CsvData)

# 入口
if __name__ == '__main__':
    Address = RinsFileAs()
    UDat = None
    # 判断返回数据是否为 tuple
    if isinstance(Address, tuple):
        CDat = RinsCfg(Address[0])
        UDat = RinsCsv(Address[1])
        SafDat = CountSafe(CDat, UDat[1])
        TaxDat = CountTax(SafDat, UDat[1])
        OutData(Address[2], UDat[0], UDat[1], SafDat, TaxDat)
        print('Success!')
    else:
        print('Er: Parameter error')