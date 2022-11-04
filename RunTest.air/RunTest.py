# -*- encoding=utf8 -*-
# 明日方舟护肝小能手
__author__ = "Kuma"
__title__ = "护肝小能手"

from airtest.core.api import *
from airtest.core.api import using
using("TestCase.air")
import TestCase

DEVICE_SELECTION = """
欢迎使用明日方舟护肝小能手\(^o^)/
请输入要使用的设备：
【1】手机
【2】Mumu模拟器
【3】夜神模拟器
【4】雷电模拟器
【5】逍遥模拟器
【6】iTools
【7】天天模拟器
【8】海马玩模拟器
【9】BlueStacks
"""

print(DEVICE_SELECTION)
while True:
    option = input("")
    if option == "1":
        dev = connect_device("Android:///")
        break
    elif option == "2":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:7555")#mumu
        break
    elif option == "3":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:62001")#夜神
        break
    elif option == "4":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:5554")#雷电
        break
    elif option == "5":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:21503")#逍遥
        break
    elif option == "6":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:54001")#iTools
        break
    elif option == "7":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:6555")#天天
        break
    elif option == "8":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:26744")#海马玩
        break
    elif option == "9":
        dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:5555")#BlueStacks
        break
    else:
        print("请输入正确的选项！！请重新输入！")
        continue

try:
    dev.minicap.get_stream()
except:
    dev = connect_device("Android:///?cap_method=JAVACAP")
    G.add_device(dev)

auto_setup(__file__)

PRINT_INFO = """
欢迎使用明日方舟护肝小能手\(^o^)/
请输入要执行操作：
【0】启动游戏
【00】启动游戏登录账号
【1】单关卡循环刷图+自动吃药（需选中关卡）
【2】剿灭用:单关卡循环刷图（需选中关卡）
【3】自动领取任务奖励（需保证界面在主页）
【4】自动获取信用（需保证界面在主页）
【5】完成公开招募领取干员（需保证界面在主页）
【6】跳过弹窗
【7】周一批量刷剿灭脚本（老图龙门市区）(剩100玉）
【8】周一批量刷剿灭脚本（新图轮换）
【9】愚人号:单关卡循环刷图（需选中关卡）
【88】退出,也可直接右上角关闭
-----------------限时活动-----------------
【001】灰蕈迷境刷蜜饼（需保证界面在活动界面）
"""

while True:
    print(PRINT_INFO)
    opear = input("")
    if "88" == opear:
        break
    elif "0" == opear:
        TestCase.StartGame()
    elif "00" == opear:
        TestCase.login_game()
    elif "1" == opear:
        print("请输入刷图次数：")
        cnt = input("")
        TestCase.AutoFight(int(cnt))
    elif "2" == opear:
        print("请输入刷图次数：")
        cnt = input("")
        TestCase.AutoFight(int(cnt),2)
    elif "3" == opear:
        TestCase.AutoMission()
    elif "4" == opear:
        TestCase.CreditAccess()
    elif "5" == opear:
        TestCase.CompleteOpenRecruitment()
    elif "6" == opear:
        TestCase.SkipPopup()
    elif "7" == opear:
        TestCase.MondayAutoFight(0)
    elif "8" == opear:
        TestCase.MondayAutoFight(1)
    elif "9" == opear:
        print("请输入刷图次数：")
        cnt = input("")
        TestCase.StultiferaNavis(int(cnt))
    elif "001" == opear:
        print("请输入刷图次数：")
        cnt = input("")
        TestCase.FungiMist(int(cnt))
    else:
        print("请输入正确的选项！！请重新输入！")
