# ArknightsAutoTest
明日方舟护肝小助手  
基于Airtest实现  [AirtestIDE-win-1.2.5](https://airtest.netease.com/download.html?download=win64/AirtestIDE-win-1.2.5.zip&&site=io "下载Airtest")
具体操作见ArknightsAutoTest教程
# 更新日志

##### 2022-5-3
1. 新增愚人号活动脚本
2. 提高脚本稳定性

##### 2022-4-14
1. 更新关卡结算界面判断图
2. 提高脚本稳定性

##### 2021-4-16
1. 新增启动游戏登录账号脚本
2. 优化兼容新UI

##### 2021-4-12
1. 新增升级判断等待

##### 2020-11-9
1. 新增新剿灭模式脚本
2. 优化退出账号脚本
3. 提高脚本稳定性

##### 2020-11-2
1. 优化脚本匹配新剿灭模式UI

##### 2020-10-29
1. 提高脚本稳定性

##### 2020-10-9
1. 增加.gitignore
2. 提高脚本稳定性

##### 2020-9-7
1. 提高脚本稳定性

##### 2020-9-4
1. 提高脚本稳定性

##### 2020-8-29
1. 新增灰蕈迷境刷蜜饼脚本，反复进出第一关刷奖励

##### 2020-8-24
1. 修改跳过弹窗函数的判断逻辑
2. 优化变量命名

##### 2020-8-20
1. 增加不同手机对minicap和javacap的兼容处理
2. 优化代码格式

##### 2020-8-19
1. 增加针对miui11以上出现minicap server setup timeout问题的特殊处理
2. 增加官方模拟器网易mumu的支持
3. 增加一键挂机剿灭功能（需添加数据配置）  
	在上级目录添加`acc.txt`文件  
	文件内格式为`"账号":"密码",#用户`

##### 2020-8-10
1. 修改理智图片识别度

##### 2020-8-7
1. 增加打开公招界面等待时间

##### 2020-8-5
1. 新增功能：公开招募完成后领取干员

##### 2020-7-27
1. 修改运行bat文件编码
2. 修复一次领取任务完成多个奖励导致脚本中断bug
3. 封装领取任务奖励为单独函数

##### 2020-7-24
1. 增加领取任务奖励判断“获得物资”隐式等待

##### 2020-7-23
1. 修复关卡选择循环未识别到“开始行动”
2. 增加领取任务奖励等待时间

##### 2020-7-21——2.1.1
1. 新增脚本：清理日志图片bat
2. 新增功能：启动游戏