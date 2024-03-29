# -*- encoding=utf8 -*-
# 明日方舟护肝小能手
__author__ = "Kuma"

from airtest.core.api import *

auto_setup(__file__)

#设置超时时长
timeout = 6000
# 获取设备的高度和宽度
width, height = device().get_current_resolution()

def WaitTouch(img,s = 0,timeout = 20):
    wait(img,timeout)
    if s :
        sleep(s)
    touch(img)
    
def OpenGame():
    start_app("com.hypergryph.arknights")
    wait(Template(r"tpl1594892913227.png", record_pos=(-0.003, 0.205), resolution=(2280, 1080)), timeout)
    touch(Template(r"tpl1594892913227.png", record_pos=(-0.003, 0.205), resolution=(2280, 1080)))
    wait(Template(r"tpl1594892983839.png", record_pos=(-0.002, 0.098), resolution=(2280, 1080)), timeout)


def StartGame():
    OpenGame()
    touch(Template(r"tpl1594892983839.png", record_pos=(-0.002, 0.098), resolution=(2280, 1080)))


def SwitchAccount(acc, pw):
    wait(Template(r"tpl1597051076287.png", record_pos=(0.228, 0.209), resolution=(2280, 1080)))
    touch(Template(r"tpl1597051076287.png", record_pos=(0.228, 0.209), resolution=(2280, 1080)))
    touch(Template(r"tpl1597051100791.png", record_pos=(-0.15, 0.095), resolution=(2280, 1080)))
    touch(Template(r"tpl1597051155115.png", target_pos=2, record_pos=(-0.002, 0.103), resolution=(2280, 1080)))
    text(acc)
    touch(Template(r"tpl1597051341386.png", record_pos=(0.431, 0.173), resolution=(2280, 1080)))
    touch(Template(r"tpl1597058496136.png", target_pos=2, record_pos=(-0.003, 0.122), resolution=(2280, 1080)))
    text(pw)
    touch(Template(r"tpl1597051341386.png", record_pos=(0.431, 0.173), resolution=(2280, 1080)))
    touch(Template(r"tpl1597058629464.png", record_pos=(-0.004, 0.142), resolution=(2280, 1080)))


def ExitAccount():
    wait(Template(r"tpl1597830778910.png", record_pos=(-0.462, -0.249), resolution=(1440, 810)))
    touch(Template(r"tpl1597830778910.png", record_pos=(-0.462, -0.249), resolution=(1440, 810)))
    #     # 获取设备的高度和宽度
    #     width, height = device().get_current_resolution()
    #     # 校准滑动的起点和终点
    #     start_pt = (width * 0.5, height / 1.2)
    #     end_pt = (width * 0.5, height / 3)
    #     swipe(start_pt,end_pt)
    wait(Template(r"tpl1608612534645.png", record_pos=(0.138, -0.088), resolution=(2400, 1080)))
    touch(Template(r"tpl1608612534645.png", record_pos=(0.138, -0.088), resolution=(2400, 1080)))
    wait(Template(r"tpl1597831642627.png", record_pos=(0.157, 0.115), resolution=(1440, 810)))
    touch(Template(r"tpl1597831642627.png", record_pos=(0.157, 0.115), resolution=(1440, 810)))


# 跳过弹窗
def SkipPopup():
    while exists(Template(r"tpl1597111964503.png", threshold=0.7, record_pos=(0.387, -0.198),
                          resolution=(2280, 1080))) or exists(
        Template(r"tpl1597112104130.png", threshold=0.9, record_pos=(0.001, -0.165), resolution=(2280, 1080))):
        if exists(Template(r"tpl1597111964503.png", record_pos=(0.387, -0.198), resolution=(2280, 1080))):
            touch(Template(r"tpl1597111964503.png", record_pos=(0.001, -0.165), resolution=(2280, 1080)))
        elif exists(Template(r"tpl1597112104130.png", record_pos=(0.001, -0.165), resolution=(2280, 1080))):
            touch(Template(r"tpl1597112104130.png", record_pos=(0.387, -0.198), resolution=(2280, 1080)))
        sleep(5)


def GoToModel4(model):
    wait(Template(r"终端.png", record_pos=(0.26, -0.155), resolution=(1440, 810)))
    touch(Template(r"终端.png", record_pos=(0.26, -0.155), resolution=(1440, 810)))
    wait(Template(r"每周部署.png", record_pos=(-0.079, 0.237), resolution=(1440, 810)))
    touch(Template(r"每周部署.png", record_pos=(-0.079, 0.237), resolution=(1440, 810)))
    sleep(5)
    if exists(Template(r"tpl1604300690305.png", record_pos=(-0.38, -0.197), resolution=(1440, 810))):
        touch(Template(r"tpl1604300690305.png", record_pos=(-0.38, -0.197), resolution=(1440, 810)))
    wait(Template(r"当期委托.png", record_pos=(0.365, -0.1), resolution=(1440, 810)))
    touch(Template(r"当期委托.png", record_pos=(0.365, -0.1), resolution=(1440, 810)))
    wait(Template(r"tpl1604301453402.png", record_pos=(-0.453, 0.224), resolution=(1440, 810)))
    sleep(3)
    if model == 1:
        pass
    else:
        keyevent("BACK")
        wait(Template(r"tpl1604299152778.png", record_pos=(0.407, 0.198), resolution=(2400, 1080)))
        touch(Template(r"tpl1604299152778.png", record_pos=(0.407, 0.198), resolution=(2400, 1080)))
        wait(Template(r"tpl1604299238209.png", threshold=0.9, record_pos=(0.301, 0.011), resolution=(2400, 1080)))
        touch(Template(r"tpl1604299238209.png", threshold=0.9, record_pos=(0.301, 0.011), resolution=(2400, 1080)))
        wait(Template(r"tpl1597829672306.png", record_pos=(0.339, -0.035), resolution=(1440, 810)))


def GoToHome():
    wait(Template(r"tpl1595558180220.png", record_pos=(-0.247, -0.209), resolution=(2280, 1080)))
    touch(Template(r"tpl1595558180220.png", record_pos=(-0.247, -0.209), resolution=(2280, 1080)))
    wait(Template(r"tpl1597830727571.png", record_pos=(-0.428, -0.078), resolution=(1440, 810)))
    touch(Template(r"tpl1597830727571.png", record_pos=(-0.428, -0.078), resolution=(1440, 810)))


def FightEnd():
    wait(Template(r"行动结束.png", threshold=0.9, record_pos=(-0.317, 0.175), resolution=(2280, 1080)), timeout)
    sleep(2)
    if exists(Template(r"tpl1600422827146.png", threshold=0.8, record_pos=(-0.182, 0.002), resolution=(2400, 1080))):
        sleep(5)
        touch(Template(r"tpl1600422827146.png", threshold=0.8, record_pos=(-0.182, 0.002), resolution=(2400, 1080)))
    touch(Template(r"行动结束.png", threshold=0.9, record_pos=(-0.317, 0.175), resolution=(2280, 1080)))


# 单关卡循环刷图+自动吃药
def AutoFight(cnt, model=1):
    if exists(Template(r"tpl1597829812232.png", record_pos=(0.332, 0.181), resolution=(1440, 810))):
        touch(Template(r"tpl1597829812232.png", record_pos=(0.332, 0.181), resolution=(1440, 810)))
    for i in range(cnt):
        wait(Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)),
             timeout=30)
        touch(Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)))
        sleep(3)
        if exists(
                Template(r"tpl1594288024016.png", threshold=0.8, record_pos=(-0.33, -0.061),
                         resolution=(2280, 1080))):
            touch(Template(r"tpl1594288083324.png", record_pos=(0.29, 0.141), resolution=(2280, 1080)))
            wait(
                Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)))
            touch(
                Template(r"tpl1594345130612.png", threshold=0.9, record_pos=(0.394, 0.19), resolution=(2280, 1080)))
        touch(Template(r"tpl1594285940292.png", record_pos=(0.304, 0.096), resolution=(2280, 1080)))
        sleep(30)
        if model == 2:  # 剿灭模式
            wait(Template(r"tpl1604310613142.png", threshold=0.8, record_pos=(0.201, -0.003), resolution=(2280, 1080)),
                 timeout)
            sleep(2)
            touch(Template(r"tpl1604310613142.png", threshold=0.8, record_pos=(0.238, -0.003), resolution=(1440, 810)))
            FightEnd()
        else:  # 主线模式
            FightEnd()


# 点击领取任务奖励
def ReceiveTaskRewards():
    while exists(Template(r"tpl1625625217664.png", record_pos=(0.374, -0.177), resolution=(1440, 810))) and not exists(
            Template(r"tpl1594346724835.png", record_pos=(0.111, 0.068), resolution=(2280, 1080))):
        touch(Template(r"tpl1625625217664.png", record_pos=(0.374, -0.177), resolution=(1440, 810)))
        sleep(3)
        if exists(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080))):
            while exists(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080))):
                touch(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))
                sleep(3)
            wait(Template(r"tpl1595558180220.png", record_pos=(-0.247, -0.209), resolution=(2280, 1080)))


# 自动领取任务奖励
def AutoMission():
    if exists(Template(r"tpl1594297049971.png", record_pos=(0.192, 0.136), resolution=(2280, 1080))):
        touch(Template(r"tpl1594297072812.png", record_pos=(0.108, 0.147), resolution=(2280, 1080)))
        sleep(3)
        ReceiveTaskRewards()
        touch(Template(r"tpl1594297174980.png", record_pos=(0.131, -0.211), resolution=(2280, 1080)))
        sleep(3)
        ReceiveTaskRewards()
        touch(Template(r"tpl1594297411538.png", record_pos=(-0.427, -0.211), resolution=(2280, 1080)))


# 自动获取信用
def CreditAccess():
    # 获取好友信用
    touch(Template(r"tpl1594601606049.png", record_pos=(-0.224, 0.143), resolution=(2280, 1080)))
    touch(Template(r"tpl1594601620037.png", record_pos=(-0.385, -0.09), resolution=(2280, 1080)))
    touch(Template(r"tpl1594601667186.png", record_pos=(0.19, 0.063), resolution=(2280, 1080)))
    wait(Template(r"tpl1599124536167.png", record_pos=(-0.424, -0.133), resolution=(1440, 810)), timeout=100)
    i = 0
    while exists(Template(r"tpl1594601712421.png", record_pos=(0.408, 0.157), resolution=(2280, 1080))):
        touch(Template(r"tpl1594601712421.png", record_pos=(0.408, 0.157), resolution=(2280, 1080)))
        sleep(4)
        wait(Template(r"tpl1599124536167.png", record_pos=(-0.424, -0.133), resolution=(1440, 810)), timeout=100)
        i = i + 1
        if i == 10:
            break
    keyevent("BACK")
    wait(Template(r"tpl1594601922513.png", threshold=0.9, record_pos=(0.154, 0.095), resolution=(2280, 1080)))
    touch(Template(r"tpl1594601922513.png", threshold=0.9, record_pos=(0.154, 0.095), resolution=(2280, 1080)))
    wait(Template(r"tpl1594601620037.png", record_pos=(-0.385, -0.09), resolution=(2280, 1080)))
    keyevent("BACK")
    # 获取采购中心信用
    wait(Template(r"tpl1594602022220.png", record_pos=(0.157, 0.084), resolution=(2280, 1080)))
    touch(Template(r"tpl1594602022220.png", record_pos=(0.157, 0.084), resolution=(2280, 1080)))
    wait(Template(r"tpl1594602046474.png", record_pos=(0.353, -0.165), resolution=(2280, 1080)))
    touch(Template(r"tpl1594602046474.png", record_pos=(0.353, -0.165), resolution=(2280, 1080)))
    if exists(Template(r"tpl1594602075044.png", record_pos=(0.293, -0.21), resolution=(2280, 1080))):
        touch(Template(r"tpl1594602075044.png", record_pos=(0.293, -0.21), resolution=(2280, 1080)))
        if exists(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080))):
            touch(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))
    # 剩下的手动购买


# 完成公开招募领取干员
def CompleteOpenRecruitment():
    if exists(Template(r"tpl1596594398713.png", record_pos=(0.324, 0.077), resolution=(2280, 1080))):
        touch(Template(r"tpl1596594398713.png", record_pos=(0.273, 0.099), resolution=(2280, 1080)))
        sleep(10)
        while exists(Template(r"tpl1596594437987.png", record_pos=(-0.207, 0.014), resolution=(2280, 1080))):
            touch(Template(r"tpl1596594437987.png", record_pos=(-0.207, 0.014), resolution=(2280, 1080)))
            wait(Template(r"tpl1596594512366.png", record_pos=(0.426, -0.208), resolution=(2280, 1080)))
            touch(Template(r"tpl1596594512366.png", record_pos=(0.426, -0.208), resolution=(2280, 1080)))
            wait(Template(r"tpl1596594609163.png", record_pos=(0.219, 0.056), resolution=(2280, 1080)))
            sleep(2)
            touch(Template(r"tpl1596594609163.png", record_pos=(0.219, 0.056), resolution=(2280, 1080)))


# 周一挂机剿灭5次
def MondayAutoFight(model):
    # 切换Yosemite输入法
    #     dev.shell("ime enable com.netease.nie.yosemite/.ime.ImeService")
    #     dev.shell("ime set com.netease.nie.yosemite/.ime.ImeService")
    OpenGame()
    # 读取配置
    f = open('./acc.txt')
    sAccConf = f.read()
    f.close()
    sAccConf = sAccConf.split('"')
    lAccConf = []
    for i in range(len(sAccConf)):
        if i % 2 != 0:
            lAccConf.append(sAccConf[i])
    # 进入循环
    for i in range(len(lAccConf)):
        if i % 2 != 0:
            acc = lAccConf[i - 1]
            pw = lAccConf[i]
            SwitchAccount(acc, pw)
            sleep(40)
            SkipPopup()
            GoToModel4(model)
            AutoFight(5, 2)
            sleep(5)
            GoToHome()
            sleep(10)
            SkipPopup()
            ExitAccount()
    # 切换Sogou输入法


#     dev.shell("ime enable com.sohu.inputmethod.sogouoem/.SogouIME")
#     dev.shell("ime set com.sohu.inputmethod.sogouoem/.SogouIME")

# 启动游戏登录账号
def login_game():
    print("请输入账号：")
    acc = input("")
    print("请输入密码：")
    pw = input("")
    OpenGame()
    SwitchAccount(acc, pw)
    sleep(40)
    SkipPopup()


# 灰蕈迷境刷蜜饼
def FungiMist(cnt):
    for i in range(cnt):
        touch(Template(r"tpl1598676865935.png", record_pos=(0.308, -0.124), resolution=(2400, 1080)))
        touch(Template(r"tpl1598676886702.png", record_pos=(-0.398, 0.025), resolution=(2400, 1080)))
        sleep(1)
        touch(Template(r"tpl1598676906075.png", threshold=0.9, record_pos=(-0.401, 0.184), resolution=(2400, 1080)))
        wait(Template(r"tpl1598676949030.png", threshold=0.9, record_pos=(-0.211, 0.109), resolution=(2400, 1080)))
        while exists(
                Template(r"tpl1598676949030.png", threshold=0.9, record_pos=(-0.211, 0.109), resolution=(2400, 1080))):
            touch(Template(r"tpl1598676949030.png", threshold=0.9, record_pos=(-0.211, 0.109), resolution=(2400, 1080)))
            touch(Template(r"tpl1599135164536.png", target_pos=9, record_pos=(-0.308, -0.22), resolution=(1440, 810)))
            touch(Template(r"tpl1598677009402.png", record_pos=(0.434, 0.193), resolution=(2400, 1080)))
            if exists(Template(r"tpl1599135248244.png", threshold=0.9, record_pos=(-0.011, 0.032),
                               resolution=(1440, 810))):
                touch(
                    Template(r"tpl1598677224290.png", threshold=0.9, record_pos=(0.174, 0.09), resolution=(2400, 1080)))
            sleep(5)
            touch(Template(r"tpl1596594609163.png", record_pos=(0.219, 0.056), resolution=(2280, 1080)))
            sleep(2)
        touch(Template(r"tpl1598677165857.png", record_pos=(0.001, 0.022), resolution=(2400, 1080)))
        wait(Template(r"tpl1598677185373.png", record_pos=(-0.146, -0.031), resolution=(2400, 1080)))
        touch(Template(r"tpl1598677185373.png", record_pos=(-0.146, -0.031), resolution=(2400, 1080)))
        touch(Template(r"tpl1598677203714.png", record_pos=(0.43, 0.058), resolution=(2400, 1080)))
        touch(Template(r"tpl1598677214926.png", record_pos=(0.386, 0.189), resolution=(2400, 1080)))
        touch(Template(r"tpl1598677224290.png", threshold=0.9, record_pos=(0.174, 0.09), resolution=(2400, 1080)))
        wait(Template(r"tpl1598677242685.png", threshold=0.9, record_pos=(-0.449, -0.193), resolution=(2400, 1080)),
             timeout=100)
        touch(Template(r"tpl1598677242685.png", record_pos=(-0.449, -0.193), resolution=(2400, 1080)))
        touch(Template(r"tpl1598677265806.png", record_pos=(0.077, -0.007), resolution=(2400, 1080)))
        sleep(1)
        touch(Template(r"tpl1598677278150.png", threshold=0.9, record_pos=(0.177, 0.09), resolution=(2400, 1080)))
        touch(Template(r"tpl1598677290047.png", record_pos=(-0.33, -0.001), resolution=(2400, 1080)))
        wait(Template(r"tpl1598685863593.png", record_pos=(-0.354, -0.062), resolution=(1440, 810)), timeout=100)
        touch(Template(r"tpl1598677314013.png", record_pos=(-0.002, -0.192), resolution=(2400, 1080)))
        wait(Template(r"tpl1598677376528.png", record_pos=(-0.001, 0.19), resolution=(2400, 1080)))
        touch(Template(r"tpl1598677376528.png", record_pos=(-0.001, 0.19), resolution=(2400, 1080)))
        wait(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))
        touch(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))
        if exists(
                Template(r"tpl1598682578919.png", threshold=0.9, record_pos=(-0.003, -0.221), resolution=(1440, 810))):
            touch(Template(r"tpl1598677376528.png", record_pos=(-0.001, 0.19), resolution=(2400, 1080)))
            wait(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))
            touch(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))


# 愚人号活动
def StultiferaNavis(cnt):
    if exists(Template(r"tpl1651716972583.png", record_pos=(0.399, 0.138), resolution=(2400, 1080))):
        touch(Template(r"tpl1651716972583.png", record_pos=(0.399, 0.138), resolution=(2400, 1080)))
    for i in range(cnt):
        wait(Template(r"tpl1651716589031.png", target_pos=7, record_pos=(0.421, 0.151), resolution=(2400, 1080)), timeout=30)
        touch(Template(r"tpl1651716589031.png", target_pos=7, record_pos=(0.421, 0.151), resolution=(2400, 1080)))
        sleep(3)
        if exists(
                Template(r"tpl1594288024016.png", threshold=0.8, record_pos=(-0.33, -0.061),
                         resolution=(2280, 1080))):
            touch(Template(r"tpl1594288083324.png", record_pos=(0.29, 0.141), resolution=(2280, 1080)))
            wait(Template(r"tpl1651716589031.png", target_pos=7, record_pos=(0.421, 0.151), resolution=(2400, 1080)))
            touch(Template(r"tpl1651716589031.png", target_pos=7, record_pos=(0.421, 0.151), resolution=(2400, 1080)))
        touch(Template(r"tpl1594285940292.png", record_pos=(0.304, 0.096), resolution=(2280, 1080)))
        sleep(30)
        FightEnd()

# 生息演算
def ReclamationAlgorithm(cnt):
    #预加载资源
    ZiYuanQu_1 = (Template(r"tpl1675217434425.png", record_pos=(-0.167, -0.102), resolution=(1280, 720)))
    ZiYuanQu_4 = (Template(r"tpl1675214931261.png", record_pos=(0.104, 0.152), resolution=(1280, 720)))
    ZiYuanQu_3_1 = (Template(r"tpl1675221778016.png", record_pos=(0.167, -0.098), resolution=(1280, 720)))
    ZiYuanQu_5_1 = (Template(r"tpl1675222591413.png", record_pos=(-0.002, -0.019), resolution=(1280, 720)))
    ZiYuanQuList = [ZiYuanQu_1,ZiYuanQu_4,ZiYuanQu_3_1,ZiYuanQu_5_1]
    p6 = (width*0.31,height*0.62)
    p1 = (width*0.33,height*0.32)
    p2 = (width*0.49,height*0.19)
    p3 = (width*0.67,height*0.33)
    p4 = (width*0.69,height*0.62)
    pList = [p6,p1,p2,p3,p4]
    #正式流程
    for i in range(cnt):
        touch(Template(r"tpl1675214261103.png", record_pos=(0.441, 0.232), resolution=(1280, 720)))
        WaitTouch(Template(r"tpl1675214315632.png", record_pos=(0.393, -0.243), resolution=(1280, 720)))
        if not exists(Template(r"tpl1675214436195.png", record_pos=(0.084, -0.172), resolution=(1280, 720))):
            touch(Template(r"tpl1675214384977.png", record_pos=(-0.138, -0.133), resolution=(1280, 720)))
            touch(Template(r"tpl1675214436195.png", record_pos=(0.084, -0.172), resolution=(1280, 720)))
            touch(Template(r"tpl1675214473576.png", record_pos=(0.252, 0.248), resolution=(1280, 720)))
        WaitTouch(Template(r"tpl1675214657274.png", record_pos=(0.34, 0.236), resolution=(1280, 720)))
        WaitTouch(Template(r"tpl1675214692482.png", record_pos=(0.313, 0.191), resolution=(1280, 720)))
        for i in range(4):
            WaitTouch(Template(r"tpl1675214740881.png", threshold=0.8, record_pos=(0.448, 0.245), resolution=(1280, 720)),2,timeout=60)
            sleep(2)
            WaitTouch(Template(r"tpl1675214811630.png", record_pos=(0.0, -0.001), resolution=(1280, 720)),4)
            for i in range(2):
                z = 0#循环参数
                o = 0#最大重复次数，超出就结束循环
                p = 0#超出最大重复后，循环寻找坐标
                while z < len(ZiYuanQuList):
                    if exists(ZiYuanQuList[i]):
                        touch(ZiYuanQuList[i])
                        break;
                    #找不到资源区的时候重新进入重新找，超过3次结束
                    if z == (len(ZiYuanQuList)-1):
                        
                        keyevent("BACK")
                        touch(Template(r"tpl1675400949440.png", record_pos=(0.443, 0.233), resolution=(1280, 720)))
                        sleep(3)
                        z = 0
                        o = o + 1
                        if o > 2:
                            #找不到资源区的时候随便点个靠下的区
                            touch((width*0.5,height*0.82))
                            break
                        continue
                    z = z + 1
                while not exists(Template(r"tpl1675214965292.png", record_pos=(0.433, 0.207), resolution=(1280, 720))):
                    keyevent("BACK")
                    keyevent("BACK")
                    touch(Template(r"tpl1675400949440.png", record_pos=(0.443, 0.233), resolution=(1280, 720)))
                    sleep(3)
                    touch(pList[p])
                    p = p + 1
                touch(Template(r"tpl1675214965292.png", record_pos=(0.433, 0.207), resolution=(1280, 720)))
                WaitTouch(Template(r"tpl1675214994413.png", record_pos=(0.372, 0.233), resolution=(1280, 720)))
                WaitTouch(Template(r"tpl1675215023667.png", record_pos=(0.382, -0.041), resolution=(1280, 720)))
                touch(Template(r"tpl1598677224290.png", threshold=0.9, record_pos=(0.174, 0.09), resolution=(2400, 1080)))
                WaitTouch(Template(r"tpl1675215113977.png", record_pos=(-0.44, -0.238), resolution=(1280, 720)),2,timeout=60)
                touch(Template(r"tpl1675215156725.png", record_pos=(0.356, 0.05), resolution=(1280, 720)))
                WaitTouch(Template(r"tpl1675215290214.png", record_pos=(-0.445, -0.045), resolution=(1280, 720)),1)
                wait(Template(r"tpl1675220050335.png", record_pos=(-0.466, -0.252), resolution=(1280, 720)))
            touch(Template(r"tpl1675215610059.png", record_pos=(0.398, -0.242), resolution=(1280, 720)))
        WaitTouch(Template(r"tpl1675214740881.png", threshold=0.8, record_pos=(0.448, 0.245), resolution=(1280, 720)),2,timeout=60)
        sleep(2)
        keyevent("BACK")
        touch(Template(r"tpl1675216481820.png", record_pos=(0.135, 0.232), resolution=(1280, 720)))
        touch(Template(r"tpl1598677224290.png", threshold=0.9, record_pos=(0.174, 0.09), resolution=(2400, 1080)))
        WaitTouch(Template(r"tpl1675216538645.png", record_pos=(0.409, 0.205), resolution=(1280, 720)))
        touch(Template(r"tpl1675216592266.png", record_pos=(0.456, 0.204), resolution=(1280, 720)))
        if exists(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080))):
            touch(Template(r"tpl1594297901838.png", record_pos=(0.004, -0.165), resolution=(2280, 1080)))

        



        


