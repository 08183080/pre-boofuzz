"""
我想要把pcap的信息提取出来,提取成csv文件
csv文件格式如下:
No.     Time    Src     Dst     protocol    length      Info
可能用到的包有?
pyshark, 
scapy, 包解析, powerful
只需要读取ip层的src和dst, tcp层的port, 应用层的ftp消息, 序号No.就好

"""

from scapy.all import *
import pyshark
import csv

"""
从path路径下读取pcap文件
根据filter条件对于pcap的众多包进行条件过滤

filter eg:
ftp                 ————————> 把所有的ftp包都提取出来了
tcp.stream eq 0     ————————> 把第一个完整的tcp流提取出来

访问数据:
Data can be accessed in multiple ways. Packets are divided into layers, 
first you have to reach the appropriate layer and then you can select your field.

"""
def read(path, filter):
    packets = pyshark.FileCapture(path, display_filter = filter)
    return packets

"""
将packet进行解析...
"""
def parse_row(packet):
    list = []
    no = packet.number
    src = packet.ip.src
    dst = packet.ip.dst
    print("no: ",no)
    print("src: ",src)
    print("dst: ",dst)
    # packet.ftp.pretty_print()
    # print(content)
    """若是ftp协议
    我目前只对于请求序列感兴趣,只提取request部分...  9/27
    """
    if packet.ftp != None:
        proto = "ftp"
        print("proto: ftp")
        if packet.ftp.request_command != None:
            ftp_request = packet.ftp.request_command 
            if packet.ftp.request_arg != None:
               ftp_request = ftp_request + " " + packet.ftp.request_arg
               print("request: ",ftp_request)
               list.append(no)
               list.append(src)
               list.append(dst)
               list.append(proto)
               list.append(ftp_request)
    return list
               
"""
发现pyshark项目:
没有找到项目里面如何获得time,如何获得info内容?
找不到类里面定义的内容的话,我就暴力提取

A: debug的时候,发现一些请求消息的一些属性的端倪...
"""

lists = []
path = "D:\\pre-boofuzz\\net-pre\\data\\6.pcap"
filter = "ftp"
packets = read(path, filter) 
# print(len(packets))       # 可以实现len()函数pr以下
for packet in packets:
    # parse_row(packet)
    # print(packet)
    try:
        list = parse_row(packet)
        lists.append(list)
    except Exception as e:
        pass
        continue

header = ['no','src','dst','proto','ftp_request']
# print(lists)
with open("./ans.csv", "a+", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(lists)

    
"""
初步实现把自定义提取的信息写入csv文件
"""
