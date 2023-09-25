# 读取
# 读取pcap文件, 将读取结果打印出来...
f = open("./data/dump1.pcap", "rb")
content = f.read()
# print(content)

# Linux上换行符是\n, 十六进制形式是\x0a
meaages = content.split(b"\x0a")

for message in meaages:
    print(message,"\n")
print(len(message))    # 324
# print(meaages[17])
# 不过wireshark打开, 有317条消息的.
"""
b'\xd4\xc3\xb2\xa1\x02\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00CO\te\xd0^\x0c\x00K\x00\x00\x00K\x00\x00\x00\x01\x00^\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00= \xb0\x00\x00\x01\x11K\xf2\xac\x11\xc0\x01\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x00)\xb8\xe0\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\xff\x00\x01CO\teE`\x0c\x00_\x00\x00\x00_\x00\x00\x0033\x00\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x86\xdd`\x0c\x9f\xb9\x00)\x11\x01\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x14\xe9\x14\xe9\x00)\xea\xf2\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\xff\x00\x01CO\te\xcab\x0c\x00K\x00\x00\x00K\x00\x00\x00\x01\x00^\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00= \xb1\x00\x00\x01\x11K\xf1\xac\x11\xc0\x01\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x00)\xb8\xe0\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\xff\x00\x01CO\te\xf5c\x0c\x00_\x00\x00\x00_\x00\x00\x0033\x00\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x86\xdd`\x0c\x9f\xb9\x00)\x11\x01\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x14\xe9\x14\xe9\x00)\xea\xf2\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\xff\x00\x01CO\te\xe8d\x0c\x00\x85\x00\x00\x00\x85\x00\x00\x0033\x00\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x86\xdd`\x0c\x9f\xb9\x00O\x11\x01\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x14\xe9\x14\xe9\x00O\x9c^\x00\x00\x84\x00\x00\x00\x00\x02\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\x1c\x00\x01\x00\x00\x00<\x00\x10\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xc0\x0c\x00\x01\x00\x01\x00\x00\x00<\x00\x04\xac\x11\xc0\x01CO\teZf\x0c\x00\x85\x00\x00\x00\x85\x00\x00\x0033\x00\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x86\xdd`\x0c\x9f\xb9\x00O\x11\x01\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x14\xe9\x14\xe9\x00O\x9c^\x00\x00\x84\x00\x00\x00\x00\x02\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\x1c\x00\x01\x00\x00\x00<\x00\x10\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xc0\x0c\x00\x01\x00\x01\x00\x00\x00<\x00\x04\xac\x11\xc0\x01CO\teeg\x0c\x00q\x00\x00\x00q\x00\x00\x00\x01\x00^\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00c \xb2\x00\x00\x01\x11K\xca\xac\x11\xc0\x01\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x00OjL\x00\x00\x84\x00\x00\x00\x00\x02\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\x1c\x00\x01\x00\x00\x00<\x00\x10\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xc0\x0c\x00\x01\x00\x01\x00\x00\x00<\x00\x04\xac\x11\xc0\x01CO\te\x94h\x0c\x00q\x00\x00\x00q\x00\x00\x00\x01\x00^\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00c \xb3\x00\x00\x01\x11K\xc9\xac\x11\xc0\x01\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x00OjL\x00\x00\x84\x00\x00\x00\x00\x02\x00\x00\x00\x00\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x05local\x00\x00\x1c\x00\x01\x00\x00\x00<\x00\x10\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xc0\x0c\x00\x01\x00\x01\x00\x00\x00<\x00\x04\xac\x11\xc0\x01CO\te\x1b\x9b\r\x00*\x00\x00\x00*\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x15]4\xfe\xb7\x08\x06\x00\x01\x08\x00\x06\x04\x00\x01\x00\x15]4\xfe\xb7\xac\x11\xc2\xee\x00\x00\x00\x00\x00\x00\xac\x11\xc0\x01CO\te\xb4\x9b\r\x00*\x00\x00\x00*\x00\x00\x00\x00\x15]4\xfe\xb7\x00\x15]\xb2\x15\x1e\x08\x06\x00\x01\x08\x00\x06\x04\x00\x02\x00\x15]\xb2\x15\x1e\xac\x11\xc0\x01\x00\x15]4\xfe\xb7\xac\x11\xc2\xeeCO\te\xbb\x9b\r\x00T\x00\x00\x00T\x00\x00\x00\x00\x15]\xb2\x15\x1e\x00\x15]4\xfe\xb7\x08\x00E\x00\x00F}D@\x00@\x11\xe2O\xac\x11\xc2\xee\xac\x11\xc0\x01\xb0-\x005\x002\xdbV\xd3\xd8\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03251\x010\x010\x03224\x07in-addr\x04arpa\x00\x00\x0c\x00\x01CO\te\x16\xa3\r\x00Z\x00\x00\x00Z\x00\x00\x00\x01\x00^\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00L \xb4\x00\x00\x01\x11K\xdf\xac\x11\xc0\x01\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x008\xc9P\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03251\x010\x010\x03224\x07in-addr\x04arpa\x05local\x00\x00\x0c\x00\x01CO\te\xb3\xa4\r\x00n\x00\x00\x00n\x00\x00\x0033\x00\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x86\xdd`\x0c\x9f\xb9\x008\x11\x01\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x14\xe9\x14\xe9\x008\xfbb\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03251\x010\x010\x03224\x07in-addr\x04arpa\x05local\x00\x00\x0c\x00\x01CO\te\x9d\xd8\r\x00\x88\x00\x00\x00\x88\x00\x00\x00\x00\x15]4\xfe\xb7\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00z%U\x00\x00\x80\x11:\x0b\xac\x11\xc0\x01\xac\x11\xc2\xee\x005\xb0-\x00f\x16\xb5\xd3\xd8\x81\x00\x00\x01\x00\x01\x00\x00\x00\x00\x03251\x010\x010\x03224\x07in-addr\x04arpa\x00\x00\x0c\x00\x01\x03251\x010\x010\x03224\x07in-addr\x04arpa\x00\x00\x0c\x00\x01\x00\x00\x00\x00\x00\x10\x04mdns\x05mcast\x03net\x00CO\te\xfc\xd8\r\x00U\x00\x00\x00U\x00\x00\x00\x00\x15]\xb2\x15\x1e\x00\x15]4\xfe\xb7\x08\x00E\x00\x00GW\xa1@\x00@\x11\x07\xf2\xac\x11\xc2\xee\xac\x11\xc0\x01\xb3*\x005\x003\xdbW\x17\xf2\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x011\x03192\x0217\x03172\x07in-addr\x04arpa\x00\x00\x0c\x00\x01CO\te\x13\x00\x0e\x00[\x00\x00\x00[\x00\x00\x00\x01\x00^\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00M \xb5\x00\x00\x01\x11K\xdd\xac\x11\xc0\x01\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x009\x8cK\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x011\x03192\x0217\x03172\x07in-addr\x04arpa\x05local\x00\x00\x0c\x00\x01CO\te+\x02\x0e\x00o\x00\x00\x00o\x00\x00\x0033\x00\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x86\xdd`\x0c\x9f\xb9\x009\x11\x01\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x14\xe9\x14\xe9\x009\xbe]\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x011\x03192\x0217\x03172\x07in-addr\x04arpa\x05local\x00\x00\x0c\x00\x01DO\tep\x1c\x0e\x00[\x00\x00\x00[\x00\x00\x00\x01\x00^\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00M \xb6\x00\x00\x01\x11K\xdc\xac\x11\xc0\x01\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x009\x8cK\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x011\x03192\x0217\x03172\x07in-addr\x04arpa\x05local\x00\x00\x0c\x00\x01DO\teC\x1e\x0e\x00o\x00\x00\x00o\x00\x00\x0033\x00\x00\x00\xfb\x00\x15]\xb2\x15\x1e\x86\xdd`\x0c\x9f\xb9\x009\x11\x01\xfe\x80\x00\x00\x00\x00\x00\x00\xa4C\x03\xf1\x1d2W\x17\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x14\xe9\x14\xe9\x009\xbe]\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x011\x03192\x0217\x03172\x07in-addr\x04arpa\x05local\x00\x00\x0c\x00\x01DO\te\xdf\x1e\x0e\x00\x85\x00\x00\x00\x85\x00\x00\x00\x00\x15]4\xfe\xb7\x00\x15]\xb2\x15\x1e\x08\x00E\x00\x00w%V\x00\x00\x80\x11:\r\xac\x11\xc0\x01\xac\x11\xc2\xee\x005\xb3*\x00c\xa4\xdf\x17\xf2\x81\x00\x00\x01\x00\x01\x00\x00\x00\x00\x011\x03192\x0217\x03172\x07in-addr\x04arpa\x00\x00\x0c\x00\x01\x011\x03192\x0217\x03172\x07in-addr\x04arpa\x00\x00\x0c\x00\x01\x00\x00\x00\x00\x00\x0b\t\xe8\xb0\xa2\xe5\x8e\x9a\xe9\xbe\x99\x00DO\te("\x0e\x00\x84\x00\x00\x00\x84\x00\x00\x00\x00\x15]\xb2\x15\x1e\x00\x15]4\xfe\xb7\x08\x00E\x00\x00vL\xb3@\x00@\x11\x12\xb1\xac\x11\xc2\xee\xac\x11\xc0\x01\xd9\xa4\x005\x00b\xdb\x86\xc5\xd6\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01b\x01f\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010
\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010\x010\x012\x010\x01f\x01f\x03ip6...
"""