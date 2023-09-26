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
    packets = pyshark.FileCapture(path, filter)
    return packets

"""
将packet进行解析...
"""
def parse_row(packet):
    no = packet.number
    src = packet['ip'].src
    dst = packet['ip'].dst
    print(no)
    print(src, "->", dst)
    packet.ftp.pretty_print()
    # print(content)
    
"""
发现pyshark项目:
没有找到项目里面如何获得time,如何获得info内容?
找不到类里面定义的内容的话,我就暴力提取
"""


path = "D:\\pre-boofuzz\\net-pre\\data\\6.pcap"
filter = "ftp"
packets = read(path, filter) 
# print(len(packets))       # 可以实现len()函数pr以下
for packet in packets:
    # parse_row(packet)
    # print(packet)
    parse_row(packet)
    break
    



