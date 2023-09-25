"""
读取wireshark导出的csv文件
将最后一列都提取出来.
"""
import csv
import random

# 读取csv文件的每一行每一列
def csv_reader(f):
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            print(e)

"""
将提取出的协议文件的序号列和最后一列的请求信息列都提取出来,以键值对的形式
我们只提取client发给server的这些数据包
"""
{"xxx:yyy","zzz:aaa"}
def csv_select(f):
    reader = csv.DictReader(f)
    dict = {}
    for row in reader:
        # 将Info信息是request开头的数据条都提取出来
        if "Request" in row["Info"]:
            dict[row['No.']] = row['Info']
        # print("insert successfully~")
    return dict

# 获取开头是Request的最后一列,同时把Request尽数删掉...
def csv_get_last(f):
    reader = csv.DictReader(f)
    list = []
    for row in reader:
        # list.append(row['Info'])
        if "Request" in row['Info']:
            list.append(row['Info'][9:])
            # print(dict['Info'])
    return list

"""
将list转换成set
"""
def list2set(list):
    s = set()
    for i in list:
        s.add(i)
    return s


"""从字典中抽取前100条数据进行处理分析"""
"字典是无序的,无法直接获得前100个数据结构,可以转换成列表之元组们"
def dict_process(dict):
    ans = []
    count = 0
    for k, v in dict.items():
        ans.append((k, v))
        count += 1
        if count == 100:
            break
    return ans


f = open("../tcpdump_cap/2.csv", "r")
# csv_reader(f)
list = csv_get_last(f)
# print(len(dict))  440 挺多的
# ans = dict_process(dict)
print(list)
s = list2set(list)
print(s)