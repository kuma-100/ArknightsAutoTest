# -*- encoding=utf8 -*-
#明日方舟护肝小能手
__author__ = "Kuma"

from airtest.core.api import *
from airtest.core.api import using
using("TestCase.air")
import TestCase

#优先连接手机，其次连接模拟器（目前仅支持网易mumu）
try:
    dev = connect_device("Android:///")
#     dev = connect_device("Android:///?cap_method=JAVACAP")
except:
    dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP^&^&ori_method=ADBORI")

#针对miui11以上出现minicap server setup timeout问题的特殊处理
# if dev.get_default_device()=="rc5dofeyhah6ibpn":#My RedmiK30 Ultra
#     print("==11==",dev.cap_method)
#     print("====",dev.minicap.get_stream())
#     del dev
#     dev = connect_device("Android:///?cap_method=JAVACAP")
#     G.add_device(dev)
#     print(dev.cap_method)
# 针对minicap
try:
    dev.minicap.get_stream()
except:
    dev = connect_device("Android:///?cap_method=JAVACAP")
    G.add_device(dev)

    
auto_setup(__file__)

opear_conf = {
    "0":"启动游戏",
    "1":"单关卡循环刷图+自动吃药（需选中关卡）",
    "2":"剿灭用:单关卡循环刷图（需选中关卡）",
    "3":"自动领取任务奖励（需保证界面在主页）",
    "4":"自动获取信用（需保证界面在主页）",
    "5":"完成公开招募领取干员（需保证界面在主页）",
    "6":"跳过弹窗",
    "7":"周一批量刷剿灭脚本",
}

print_info = """
欢迎使用明日方舟护肝小能手\(^o^)/
请输入要执行操作：
【0】启动游戏
【1】单关卡循环刷图+自动吃药（需选中关卡）
【2】剿灭用:单关卡循环刷图（需选中关卡）
【3】自动领取任务奖励（需保证界面在主页）
【4】自动获取信用（需保证界面在主页）
【5】完成公开招募领取干员（需保证界面在主页）
【6】跳过弹窗
【7】周一批量刷剿灭脚本
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
        print("===222======",dev.cap_method)
        TestCase.StartGame()
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
    if "5" == opear:
        TestCase.CompleteOpenRecruitment()
    if "6" == opear:
        TestCase.SkipPopup()
    if "7" == opear:
        #切换Yosemite输入法
        dev.shell("ime enable com.netease.nie.yosemite/.ime.ImeService")
        dev.shell("ime set com.netease.nie.yosemite/.ime.ImeService")
        TestCase.MondayAutoFight()
        #切换Sogou输入法
        dev.shell("ime enable com.sohu.inputmethod.sogouoem/.SogouIME")
        dev.shell("ime set com.sohu.inputmethod.sogouoem/.SogouIME")
        
