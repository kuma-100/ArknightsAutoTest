# -*- encoding=utf8 -*-
#明日方舟护肝小能手
__author__ = "Kuma"

from airtest.core.api import *

auto_setup(__file__)

timeout=6000

#单关卡循环刷图+自动吃药
def AutoFight(cnt,model=1):
    for i in range(cnt):
        wait(Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)))
        touch(Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)))

        if exists(Template(r"tpl1594288024016.png", record_pos=(-0.33, -0.061), resolution=(2280, 1080))):
            touch(Template(r"tpl1594288083324.png", record_pos=(0.29, 0.141), resolution=(2280, 1080)))
            wait(Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)))
            touch(Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)))
        touch(Template(r"tpl1594285940292.png", record_pos=(0.304, 0.096), resolution=(2280, 1080)))
        sleep(30)
        if model == 1:
            wait(Template(r"tpl1594286088698.png", record_pos=(-0.317, 0.175), resolution=(2280, 1080)),timeout)
            sleep(2)
            touch(Template(r"tpl1594286088698.png", record_pos=(-0.317, 0.175), resolution=(2280, 1080)))
        if model == 4:
            wait(Template(r"tpl1594605537877.png", threshold=0.9, record_pos=(0.201, -0.003), resolution=(2280, 1080)),timeout)
            touch(Template(r"tpl1594605537877.png", record_pos=(0.201, -0.003), resolution=(2280, 1080)))
            wait(Template(r"tpl1594286088698.png", record_pos=(-0.317, 0.175), resolution=(2280, 1080)))
            sleep(2)
            touch(Template(r"tpl1594286088698.png", record_pos=(-0.317, 0.175), resolution=(2280, 1080)))

#点击领取任务奖励
def ReceiveTaskRewards():
    while exists(Template(r"tpl1594297115457.png", threshold=0.9, record_pos=(0.277, -0.143), resolution=(2280, 1080))) and not exists(Template(r"tpl1594346724835.png", record_pos=(0.111, 0.068), resolution=(2280, 1080))):
        touch(Template(r"tpl1594297115457.png", record_pos=(0.277, -0.143), resolution=(2280, 1080)))
        sleep(3)
        if exists(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080))):
            while exists(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080))):
                touch(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))
                sleep(3)
            wait(Template(r"tpl1595558180220.png", record_pos=(-0.247, -0.209), resolution=(2280, 1080)))
            
#自动领取任务奖励
def AutoMission():
    if exists(Template(r"tpl1594297049971.png", record_pos=(0.192, 0.136), resolution=(2280, 1080))):
        touch(Template(r"tpl1594297072812.png", record_pos=(0.108, 0.147), resolution=(2280, 1080)))
        sleep(3)
        ReceiveTaskRewards()
        touch(Template(r"tpl1594297174980.png", record_pos=(0.131, -0.211), resolution=(2280, 1080)))
        sleep(3)
        ReceiveTaskRewards()
        touch(Template(r"tpl1594297411538.png", record_pos=(-0.427, -0.211), resolution=(2280, 1080)))

#自动获取信用
def CreditAccess():
    #获取好友信用
    touch(Template(r"tpl1594601606049.png", record_pos=(-0.224, 0.143), resolution=(2280, 1080)))
    touch(Template(r"tpl1594601620037.png", record_pos=(-0.385, -0.09), resolution=(2280, 1080)))
    touch(Template(r"tpl1594601667186.png", record_pos=(0.19, 0.063), resolution=(2280, 1080)))
    sleep(4)
    while exists(Template(r"tpl1594601712421.png", record_pos=(0.408, 0.157), resolution=(2280, 1080))):
        touch(Template(r"tpl1594601712421.png", record_pos=(0.408, 0.157), resolution=(2280, 1080)))
        sleep(4)
    touch(Template(r"tpl1594297411538.png", record_pos=(-0.427, -0.211), resolution=(2280, 1080)))
    touch(Template(r"tpl1594601922513.png", record_pos=(0.154, 0.095), resolution=(2280, 1080)))
    sleep(3)
    touch(Template(r"tpl1594297411538.png", record_pos=(-0.427, -0.211), resolution=(2280, 1080)))
    #获取采购中心信用
    touch(Template(r"tpl1594602022220.png", record_pos=(0.157, 0.084), resolution=(2280, 1080)))
    touch(Template(r"tpl1594602046474.png", record_pos=(0.353, -0.165), resolution=(2280, 1080)))
    if  exists(Template(r"tpl1594602075044.png", record_pos=(0.293, -0.21), resolution=(2280, 1080))):
        touch(Template(r"tpl1594602075044.png", record_pos=(0.293, -0.21), resolution=(2280, 1080)))
        if exists(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080))):
            touch(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))
    #剩下的手动购买
    
def start_game():
    start_app("com.hypergryph.arknights")
    wait(Template(r"tpl1594892913227.png", record_pos=(-0.003, 0.205), resolution=(2280, 1080)),timeout)
    touch(Template(r"tpl1594892913227.png", record_pos=(-0.003, 0.205), resolution=(2280, 1080)))
    wait(Template(r"tpl1594892983839.png", record_pos=(-0.002, 0.098), resolution=(2280, 1080)),timeout)
    touch(Template(r"tpl1594892983839.png", record_pos=(-0.002, 0.098), resolution=(2280, 1080)))

#完成公开招募领取干员
def CompleteOpenRecruitment():
    if exists(Template(r"tpl1596594372082.png", record_pos=(0.324, 0.077), resolution=(2280, 1080))):
        touch(Template(r"tpl1596594398713.png", record_pos=(0.273, 0.099), resolution=(2280, 1080)))
        while exists(Template(r"tpl1596594437987.png", record_pos=(-0.207, 0.014), resolution=(2280, 1080))):
            touch(Template(r"tpl1596594437987.png", record_pos=(-0.207, 0.014), resolution=(2280, 1080)))
            wait(Template(r"tpl1596594512366.png", record_pos=(0.426, -0.208), resolution=(2280, 1080)))
            touch(Template(r"tpl1596594512366.png", record_pos=(0.426, -0.208), resolution=(2280, 1080)))
            touch(Template(r"tpl1596594609163.png", record_pos=(0.219, 0.056), resolution=(2280, 1080)))




        




