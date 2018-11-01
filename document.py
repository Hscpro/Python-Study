#!/usr/bin/env pyhon3

# 打印行数
"""
with open('./document.txt') as file:
    count = 0
    for line in file:
        count += 1
    print(count)
"""

# 读取内容
"""
with open('./document.txt') as file:
    print(file.read())
"""

# 文件内容统计
"""
filename = input("Enter the file name: ")
with open(filename) as file:
    count = 0
    for line in file:
        count += 1
        print(line)
    print('Lines:', count)
"""

# 写入内容 覆盖
"""
filename = './document.txt'
with open(filename, 'a') as file: # w-覆盖 a-追加
    file.write('testline1')
    file.write('testline1')
"""

# 拷贝文件
"""
import sys
def copy_file(src, dst):                        #拷贝函数
    with open(src, 'r') as src_file:            #以读模式打开文件src - src_file
        with open(dst, 'w') as dst_file:        #以写模式打开文件dst - dst_file
            dst_file.write(src_file.read())     #把src_file的内容覆盖写到dst_file
if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1], sys.argv[2])
    else:
        print("Parameter Error")
        print(sys.argv[0], "srcfile dstfile")
        sys.exit(-1)
    sys.exit(0)
"""

# pickle 模块将 Python 的一个字典存入到文件中并读取出来恢复成字典对象
"""
import pickle
courses = {1:'Linux', 2:'Vim', 3:'Git'}
with open('./document.txt', 'wb') as file:
    pickle.dump(courses, file)
with open('./document.txt', 'rb') as file:
    new_coueses = pickle.load(file)
print(new_coueses)
"""

# JSON 模块
"""
import json
courses = {1:'Linux', 2:'Vim', 3:'Git'}

with open('./document.json', 'w') as file:
    file.write(json.dumps(courses))
with open('./document.json', 'w') as file:
    json.dump(courses, file)

print(json.loads(json.dumps(courses)))
with open('./document.json', 'r') as file:
    print(json.load(file))
"""

# 使用 JSON 序列化数据到文件中
import json
with open('./document.json', 'r') as data:
    data = json.dumps(data.read())
print(data)
with open('./document.json', 'w') as file:
    json.dump(data, file)

# CSV 文件读写
