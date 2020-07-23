# -*- encoding=utf8 -*-
#明日方舟护肝小能手
__author__ = "Kuma"

from airtest.core.api import *
from airtest.core.api import using
using("TestCase.air")
import TestCase

auto_setup(__file__,devices=["Android:///"])

opear_conf = {
    "0":"启动游戏",
    "1":"单关卡循环刷图+自动吃药（需选中关卡）",
    "2":"剿灭用:单关卡循环刷图（需选中关卡）",
    "3":"自动领取任务奖励（需保证界面在主页）",
    "4":"自动获取信用（需保证界面在主页）",
}

print_info = """
欢迎使用明日方舟护肝小能手\(^o^)/
请输入要执行操作：
【0】启动游戏
【1】单关卡循环刷图+自动吃药（需选中关卡）
【2】剿灭用:单关卡循环刷图（需选中关卡）
【3】自动领取任务奖励（需保证界面在主页）
【4】自动获取信用（需保证界面在主页）
【88】退出,也可直接右上角关闭
"""

while True:
    print(print_info)
    opear = input("")
    if "88" == opear:
        break
    if not opear_conf.__contains__(opear):
        print("请输入正确的选项！！请重新输入！")
        continue
    if "0" == opear:
        TestCase.start_game()
    if "1" == opear:
        print("请输入刷图次数：")
        cnt = input("")
        TestCase.AutoFight(int(cnt))
    if "2" == opear:
        print("请输入刷图次数：")
        cnt = input("")
        TestCase.AutoFight(int(cnt),4)
    if "3" == opear:
        TestCase.AutoMission()
    if "4" == opear:
        TestCase.CreditAccess()

    


#执行脚本,使用时把对应行代码前的#字去掉，不需要使用时把#加上，每次只能跑一个指令
#单关卡循环刷图+自动吃药，括号内数字为次数，剿灭model为4
#TestCase.AutoFight(5)
#TestCase.AutoFight(4,4)#剿灭用，每周一日常跑
#自动领取任务奖励
#TestCase.AutoMission()
#自动获取信用
#TestCase.CreditAccess()