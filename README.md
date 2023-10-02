# pre-boofuzz
结合机器学习，协议逆向，对于boofuzz的改进...

# pre 资源
1. [Pre list](https://github.com/techge/PRE-list) 对于网络协议的自动化逆向的工具、方法论、方法.

# 协议 介绍
1. [FTP rfc](https://datatracker.ietf.org/doc/html/rfc959)

# TO DO
- [x] 数据收集
  - [x] 收集很多的不同账户的登录信息发送ftp数据包
- [ ] 查看很多种ftp协议的漏洞
- [ ] 通过聚类将请求包分成n类, 再通过最长公共子序列算法提取出请求格式
- [ ] 设计一种从很多的协议流信息中提取出状态机的算法
- [ ] 先完成自动化针对于FTP协议的状态机的推理（针对于wireshark抓和解析的包）
- [ ] 首先实现一个自动化的针对于FTP协议的网络流逆向工具【FTP协议状态机推理器】
- [ ] 完成针对于ftp的协议状态机构建之后,在boofuzz上集成起来,浅浅跑一跑
- [ ] 整体设计，写个研究计划

# 项目日志
## net-pre
走得再慢一点，走得再稳一点。[【日志】](https://github.com/08183080/pre-boofuzz/tree/main/net-pre)

# 问题思考
1. Boofuzz的缺点是什么？

# 阅读的相关论文