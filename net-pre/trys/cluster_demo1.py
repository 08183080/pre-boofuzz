# 设计一种报文聚类算法
# 字符串版本的报文聚类, 譬如说我这里有一系列的命令吧
# User dragon、pwd等等, 我想要让他们各自聚类,有没有一种很合适的算法?
# 目前我只想专注于对ftp协议的报文流量的聚类分析
# 我想先从wireshark辅助逆向出来的字符串层面, 进行逆向分析...

"""
Q: 字符串的聚类算法有哪些?
1. K-Means算法
2. 层次聚类算法
"""
# pip install numpy -i 'https://pypi.tuna.tsinghua.edu.cn/simple'
# pip install scikit-learn
# 层次聚类 demo

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.cluster import AgglomerativeClustering
import csv_reader
from longest_common_str import find_lcsubstr

# 输入字符串列表
# strings = [
#     'USER dragon',
#     'USER luffy',
#     'USER kitty',
#     'PWD',
#     'SYST',
#     'PASS 10234',
#     'SYST',
#     'USER ***',
#     'PASS 0000000',
#     'User XieHoulong'
# ]
f = open("../data/2.csv", "r")
strings = csv_reader.csv_get_last(f)
print(strings)

# 计算字符串之间的相似度矩阵
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(strings)
distances = pairwise_distances(tfidf_matrix, metric='cosine')

# 执行层次聚类
n_clusters = 9  # 聚类数目
clustering = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='average')
clustering.fit(distances)

# 输出聚类结果
clusters = [[] for _ in range(n_clusters)]
for i, label in enumerate(clustering.labels_):
    clusters[label].append(strings[i])

for i, cluster in enumerate(clusters):
    print(f'Cluster {i + 1}: {cluster}')

# print(clusters)
for i in range(n_clusters):
    n = len(clusters[i])
    s1 = clusters[i][0]
    s2 = clusters[i][n-1] if n >= 1 else s1
    pattern = find_lcsubstr(s1, s2)
    print(f"cluster{i+1}的请求包格式是: {find_lcsubstr(s1, s2)[0]}", " xxx")