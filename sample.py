import tkinter as tk
from canv_pkg import *



#界面基础属性
robot=tk.Tk()
robot.geometry("800x500")
robot.title("智能机器人")

#底层画布
canvas=tk.Canvas(robot,width=800,height=500,highlightthickness=0)
bg = tk.PhotoImage(file='background.png')
canvas.create_image(400,250,image=bg)
canvas.pack()

#按钮存储列表
btn_list=[]

def win_empty():
    global btn_list
    for i in btn_list:
        i.destroy()
    btn_list=[]

def fun():
    print(11)

#界面方法
#example
btn1=Button_Canvas(x1=300,y1=300,x2=500,y2=400,text='开始',canvas=canvas,func=fun)







#运行
robot.mainloop()