import tkinter as tk
from canv_pkg import *
from weather import get_weather
from pygame import mixer
import time

#声音初始化
mixer.init()
btn=mixer.Sound('button.mp3')  

#界面基础属性
robot=tk.Tk()
robot.geometry("800x500")
#robot.attributes("-fullscreen", True)
robot.title("智能机器人")

#底层画布
canvas=tk.Canvas(robot,width=800,height=500,highlightthickness=0)
bg = tk.PhotoImage(file='background.png')
canvas.create_image(400,250,image=bg)
canvas.pack()

#按钮存储列表
state=''

def win_empty():
    global state
    canvas.delete(state)
    state=''

#界面方法
#example
#btn1=Button_Canvas(x1=300,y1=300,x2=500,y2=400,text='开始',canvas=canvas,func=fun)

def main_win():
    global state
    btn.play()
    win_empty()
    state='main_win'
    tag='main_win'
    btn1=Button_Canvas(x1=50,y1=100,x2=250,y2=200,text='介绍',canvas=canvas,func=intro,tag=[tag,'btn1'])
    btn2=Button_Canvas(x1=300,y1=100,x2=500,y2=200,text='环境数据',canvas=canvas,func=environ,tag=[tag,'btn2'])
    btn3=Button_Canvas(x1=550,y1=100,x2=750,y2=200,text='导航',canvas=canvas,func=navi,tag=[tag,'btn3'])
    btn4=Button_Canvas(x1=50,y1=300,x2=250,y2=400,text='来访',canvas=canvas,func=visit,tag=[tag,'btn4'])
    btn5=Button_Canvas(x1=300,y1=300,x2=500,y2=400,text='签名板',canvas=canvas,func=sign,tag=[tag,'btn5'])
    btn6=Button_Canvas(x1=550,y1=300,x2=750,y2=400,text='屏保',canvas=canvas,func=desktop,tag=[tag,'btn6'])
    btn7=Button_Canvas(x1=750,y1=440,x2=790,y2=490,text='退出',canvas=canvas,func=quit,tag=[tag,'btn7'])
    
def quit():
    btn.play()
    time.sleep(0.2)
    robot.quit()

def intro():
    global state
    btn.play()
    win_empty()
    state='intro'
    tag='intro'
    btn1=Button_Canvas(x1=50,y1=200,x2=250,y2=300,text='自我介绍',canvas=canvas,func=self_intro,tag=[tag,'btn1'])
    btn2=Button_Canvas(x1=300,y1=200,x2=500,y2=300,text='学校简介',canvas=canvas,func=sch_intro,tag=[tag,'btn2'])
    btn3=Button_Canvas(x1=550,y1=200,x2=750,y2=300,text='毕业生去向',canvas=canvas,func=grdu,tag=[tag,'btn3'])
    btn4=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=main_win,tag=[tag,'btn4'])
    text=canvas.create_text(100,100,text='介绍',font=('Arial',40,'bold'),fill='black',tag=[tag])

def self_intro():
    global state
    btn.play()
    win_empty()
    state='self_intro'
    tag='self_intro'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=intro,tag=[tag,'btn1'])
    text1=canvas.create_text(100,100,text='自我介绍',font=('Arial',40,'bold'),fill='black',tag=[tag])
    txt='我是由北京王府学校2024届毕业生自主\n开发的校园智能导引服务一体化集成系统助手小\n王。我可以为您提供导航，介绍，答疑等服务。'
    text2=canvas.create_text(400,200,text=txt,font=('Arial',20,'bold'),fill='black',tag=[tag])
    

def sch_intro():
    global state
    btn.play()
    win_empty()
    state='sch_intro'
    tag='sch_intro'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=intro,tag=[tag,'btn1'])
    text1=canvas.create_text(100,100,text='学校简介',font=('Arial',40,'bold'),fill='black',tag=[tag])

def grdu():
    global state
    btn.play()
    win_empty()
    state='grdu'
    tag='grdu'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=intro,tag=[tag,'btn1'])
    text1=canvas.create_text(100,100,text='毕业生去向',font=('Arial',40,'bold'),fill='black',tag=[tag])
    txt='今年王府学子们硕果累累，\n用出色的学术水平和多元的课外活动赢得世界顶级大学的青睐。\n24届毕业生斩获qs世界排名top50大学共（）枚offer，\nus news前50大学（）枚offer。\n录取学校包括但不限于伦敦大学学院，\n北卡罗莱纳大学教堂山分校，南加州大学，\n香港大学等世界顶尖学府。除了王府学子们的拼搏，\n这个圆满的申请季离不开老师们的精心教导和领导们的英明决策。'
    text2=canvas.create_text(400,200,text=txt,font=('Arial',20,'bold'),fill='black',tag=[tag])


def environ():
    global state
    btn.play()
    win_empty()
    state='environ'
    tag='environ'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=main_win,tag=[tag,'btn1'])
    text1=canvas.create_text(100,100,text='环境数据',font=('Arial',40,'bold'),fill='black',tag=[tag])
    txt=get_weather('北京')
    text2=canvas.create_text(400,200,text=txt,font=('Arial',20,'bold'),fill='black',tag=[tag])


def navi():
    global state
    btn.play()
    win_empty()
    state='navi'
    tag='navi'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=main_win,tag=[tag,'btn1'])
    btn2=Button_Canvas(x1=300,y1=200,x2=500,y2=300,text='Demo',canvas=canvas,func=demo,tag=[tag,'btn2'])
    text1=canvas.create_text(100,100,text='导航',font=('Arial',40,'bold'),fill='black',tag=[tag])

def demo():
    global state
    btn.play()
    win_empty()
    state='demo'
    tag='demo'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=navi,tag=[tag,'btn1'])
    text1=canvas.create_text(100,100,text='1302',font=('Arial',40,'bold'),fill='black',tag=[tag])
    txt='请您出门左转，\n沿着走廊一直走到1号楼，\n再右转就能看到1302教室在您的右手边。'
    text2=canvas.create_text(400,200,text=txt,font=('Arial',20,'bold'),fill='black',tag=[tag])


def visit():
    global state
    btn.play()
    win_empty()
    state='visit'
    tag='visit'
    btn1=Button_Canvas(x1=50,y1=200,x2=250,y2=300,text='礼品',canvas=canvas,func=gift,tag=[tag,'btn1'])
    btn2=Button_Canvas(x1=300,y1=200,x2=500,y2=300,text='留言板',canvas=canvas,func=comment,tag=[tag,'btn2'])
    btn3=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=main_win,tag=[tag,'btn3'])
    text1=canvas.create_text(100,100,text='来访',font=('Arial',40,'bold'),fill='black',tag=[tag])
    
def gift():
    global state
    btn.play()
    win_empty()
    state='gift'
    tag='gift'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=visit,tag=[tag,'btn1'])
    text1=canvas.create_text(400,200,text='请收下这份礼物',font=('Arial',40,'bold'),fill='black',tag=[tag])

def comment():
    global state
    btn.play()
    win_empty()
    state='comment'
    tag='comment'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=visit,tag=[tag,'btn1'])
    btn2=Button_Canvas(x1=300,y1=400,x2=500,y2=490,text='留言完毕',canvas=canvas,func=thanks,tag=[tag,'btn2'])
    text1=canvas.create_text(100,100,text='留言板',font=('Arial',40,'bold'),fill='black',tag=[tag])

def thanks():
    global state
    btn.play()
    win_empty()
    state='thanks'
    tag='thanks'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=main_win,tag=[tag,'btn1'])
    text1=canvas.create_text(400,200,text='感谢您的留言！',font=('Arial',40,'bold'),fill='black',tag=[tag])

def sign():
    global state
    btn.play()
    win_empty()
    state='sign'
    tag='sign'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=main_win,tag=[tag,'btn1'])
    btn2=Button_Canvas(x1=300,y1=400,x2=500,y2=450,text='签名完毕',canvas=canvas,func=main_win,tag=[tag,'btn2'])
    text1=canvas.create_text(100,100,text='签名板',font=('Arial',40,'bold'),fill='black',tag=[tag])

def desktop():
    global state
    btn.play()
    win_empty()
    state='desktop'
    tag='desktop'
    btn1=Button_Canvas(x1=600,y1=400,x2=750,y2=450,text='返回',canvas=canvas,func=main_win,tag=[tag,'btn1'])


main_win()


#运行
robot.mainloop()