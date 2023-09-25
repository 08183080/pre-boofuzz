import Levenshtein

s1 = "User dragon"
s2 = "User luffy"
s3 = "User xxx"
# 编辑距离，描述由一个字串转化成另一个字串最少的操作次数，在其中的操作包括 插入、删除、替换
# 距离计算的metric, 是聚类的前提标准之一
distance =  Levenshtein.distance(s1, s2)  # 6
print("distance between s1 an s2: ", distance)

# 改头换面, 终不似旧日模样
s4 = "亿万身家"
s5 = "一穷二白"
# print(len(s4))
distance2 = Levenshtein.distance(s3, s4) # 8
print("distance between s3 and s4: ", distance2)