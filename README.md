# 介绍
**输入**

./input/ips.txt 检测目标，必须带上协议（http/ssh/mysql/ftp 等），可直接粘贴 CheckPorts 结果

**输出**

./output/ 
- out_web.txt : 调用 dirsearch 目录猜测结果，默认字典仅检测高危目录
- out_sys.txt : 调用 Hydra 等其他工具对系统端口服务的测试结果
    

# 依赖
需要本地安装 hydra

# CheckTools 介绍（流程）

![checkSOP.png](https://i.loli.net/2019/10/14/RYdcAXeLZMaJrFu.png)