# 2023
## 9月
不要因为别人提前交卷，自己就乱答题。
如果你已经把一手好牌打烂，那就再把它打好。
- [ ] 【目标】初步实现ftp的pcap2fsm的工具出来
- [x] 9/25【github项目构建】将这个项目构建到github，实验室拉取下来，简单跑了跑【聚类】+【LCS】->【请求模式】
- [ ] 9/26【数据收集 和 思路设计】
  - [x] adduser创建数个账户，crtl+c完整收集数据包，数据包收集的很完善了。
  - [x] 使用wireshark工具的时候，发现ctrl+alt+shift+t可以追踪每一条ftp的slow。
  - [ ] 阅读ftp协议，理解它的状态机。
  - [ ] 捋清楚我想做的改进的可行性。
  - [x] 尝试实现py2csv，还有一些没解决，发现[pyshark](https://github.com/KimiNewt/pyshark)开源项目还有不足，可以去PR
