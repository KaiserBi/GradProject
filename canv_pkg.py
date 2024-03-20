from tkinter import *
import time
from PIL import Image, ImageTk, ImageGrab
class Button_Canvas:
    ## ------- 画布按钮类 ------- ##
    def __init__(self,canvas:Canvas,x1:int,y1:int,x2:int,y2:int,text:str,fontsize:int=15,d_outline:str='blue',d_fill:str='blue',image:PhotoImage=None,func=any,tag=any):
        self.canvas = canvas#父控件
        self.value = text
        self.tag = tag
        self.func=func

        self.x1 = x1#左上角x坐标
        self.y1 = y1#左上角y坐标
        self.x2 = x2#右下角x坐标
        self.y2 = y2#右下角y坐标
        self.d_outline = d_outline#默认外框颜色
        self.d_fill = d_fill#默认文字颜色

        self.rec = self.canvas.create_rectangle(x1,y1,x2,y2,width=2,outline=self.d_outline,tag=self.tag)
        self.tex = self.canvas.create_text((x1+x2)//2,(y1+y2)//2,text=self.value,font=('楷体',fontsize),justify='center',fill=self.d_fill,tag=self.tag)
        self.line=self.canvas.create_line(x1,(y1+y2)/2,x2,(y1+y2)/2,width=y2-y1,fill='',tag=self.tag)
        
        self.canvas.tag_bind(self.tag[1],'<Button-1>',lambda event:self.focus_on(self.func))# 关联鼠标点击事件
        self.canvas.tag_bind(self.tag[1],'<Motion>',lambda event:self.Move(event,'black'))# 关联鼠标经过事件
        
        if image != None:
            self.canvas.create_image((x1+x2)//2,(y1+y2)//2,image=image)

    def focus_on(self,func):
        ## ------ 焦点已获取状态 ------ ##
        #self.canvas.itemconfig(self.rec,fill=color)
        return func()

    def move_on(self,color:str):
        ## ------ 焦点半获取状态 ------ ##
        self.canvas.itemconfig(self.rec,outline=color)
        self.canvas.itemconfig(self.tex,fill=color)
    
    def move_off(self):
        ## ------ 焦点非半获取状态 ------ ##
        self.canvas.itemconfig(self.rec,outline=self.d_outline)
        self.canvas.itemconfig(self.tex,fill=self.d_fill)
    
    def Move(self,event:Event,color:str):
        ## ------ 焦点半获取状态检测 ------ ##
        if self.x1+10<=event.x<=self.x2-10 and self.y1+10<=event.y<=self.y2-10:
            self.move_on(color)
        else:
            self.move_off()

    def execute(self,event:Event,function=None):
        ## ------- 执行关联函数 ------- ##
        if self.x1<=event.x<=self.x2 and self.y1<=event.y<=self.y2:
            self.focus_off()
            self.move_off()
            
            if function != None:
                return function()

    def value_change(self,value:str):
        ## ------ 显示值改变 ------ ##
        self.value = value
        self.canvas.itemconfig(self.tex,text=self.value)

    def destroy(self):
        ## ------ 按钮删除 ------ ##
        self.canvas.delete(self.tag)
        
class Entry_Canvas:
    ## ------- 画布文本框类 ------- ##
    def __init__(self,canvas:Canvas,x:int,y:int,r_width:int,r_height:int,text1:str,text2:str,pw_mode:bool=False,d_outline:str='gray',d_fill:str='gray',fontsize:int=15):
        self.canvas = canvas#父控件
        self.focus = False#是否获取到当前焦点
        self.mode = pw_mode#密码模式

        self.value = ''#真实值
        self.info = ''#表面值

        self.x1 = x-r_width#左上角x坐标
        self.y1 = y-r_height#左上角y坐标
        self.x2 = x+r_width#右下角x坐标
        self.y2 = y+r_height#右下角y坐标
        self.info1 = text1#未获取焦点时文本显示
        self.info2 = text2#半获取焦点时文本显示
        self.d_outline = d_outline#默认外框颜色
        self.d_fill = d_fill#默认文字颜色

        self.rec = self.canvas.create_rectangle(x-r_width,y-r_height,x+r_width,y+r_height,width=2,outline=d_outline)
        self.tex = self.canvas.create_text(x,y,text=self.info1,font=('楷体',fontsize),fill=d_fill)

    def focus_on(self,color:str):
        ## ------ 焦点已获取状态 ------ ##
        self.focus = True
        self.canvas.itemconfig(self.rec,outline=color)
        self.canvas.itemconfig(self.tex,text=self.info+'|')

    def focus_off(self):
        ## ------ 焦点未获取状态 ------ ##
        self.focus = False
        self.canvas.itemconfig(self.rec,outline=self.d_outline)

        if self.info == '':
            self.canvas.itemconfig(self.tex,text=self.info1)
        else:
            self.canvas.itemconfig(self.tex,text=self.info)
    
    def Focus(self,event:Event,color:str='white'):
        ## ------- 焦点获取状态检测 ------- ##
        if self.x1<=event.x<=self.x2 and self.y1<=event.y<=self.y2:
            self.focus_on(color)
        else:
            self.focus_off()

    def move_on(self,color:str):
        ## ------ 焦点半获取状态 ------ ##
        if self.focus == False:
            self.canvas.itemconfig(self.rec,outline=color)
            if self.canvas.itemcget(self.tex,'text') == self.info1:
                self.canvas.itemconfig(self.tex,text=self.info2)
    
    def move_off(self):
        ## ------ 焦点非半获取状态 ------ ##
        if self.focus == False:
            self.canvas.itemconfig(self.rec,outline=self.d_fill)
            if self.canvas.itemcget(self.tex,'text') == self.info2:
                self.canvas.itemconfig(self.tex,text=self.info1)

    def Move(self,event:Event,color:str='white'):
        ## ------- 焦点半获取状态检测 ------- ##
        if self.x1<=event.x<=self.x2 and self.y1<=event.y<=self.y2:
            self.move_on(color)
        else:
            self.move_off()

    def input(self,char:str,length:int=10):
        ## ------ 文本输入 ------ ##
        if self.focus == True:
            
            value = ord(char)
            if value == 8:
                self.value = self.value[:-1]
            elif value<=47 or 58<=value<=64 or 91<=value<=96 or 123<=value<=256:
                pass
            else:
                if len(self.value) < length and not char.isspace():
                    self.value += char

            if self.mode == True:
                self.info = '•'*len(self.value)
            else:
                self.info = self.value

            self.canvas.itemconfig(self.tex,text=self.info+'|')


class Draw_Canvas:
    def __init__(self,canvas:Canvas,x1:int,y1:int,x2:int,y2:int,color:str='white',tag=any,path:str=''):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.tag = tag
        self.line = self.canvas.create_line(x1,(y1+y2)/2,x2,(y1+y2)/2,width=y2-y1,fill=self.color,tag=self.tag)
        self.path=path
        self.yesno = IntVar(value=0)
        self.what = IntVar(value=1)
        self.X = IntVar(value=0)
        self.Y = IntVar(value=0)

        self.foreColor = '#000000'
        self.backColor = '#FFFFFF'

        self.lastDraw = 50
        self.end = [50]
        self.size = "1000"

        self.canvas.tag_bind(self.tag[1],'<Button-1>', self.onLeftButtonDown)
        self.canvas.tag_bind(self.tag[1],'<B1-Motion>', self.onLeftButtonMove)
        self.canvas.tag_bind(self.tag[1],'<ButtonRelease-1>', self.onLeftButtonUp)

    def getter(self,widget):
        time.sleep(0.5)
        
        x11=(self.canvas.winfo_rootx()+self.x1)*2
        y11=(self.canvas.winfo_rooty()+self.y1)*2
        x22=(self.canvas.winfo_rootx()+self.x2)*2
        y22=(self.canvas.winfo_rooty()+self.y2)*2
        
        filename =self.path+'/'+str(time.time())+'.png'
        img=ImageGrab.grab().crop((x11, y11, x22, y22))
        img=img.convert('RGB')
        img.save(filename)
    
    def onLeftButtonDown(self,event):
        self.yesno.set(1)
        self.X.set(event.x)
        self.Y.set(event.y)
        if self.what.get() == 4:
            self.canvas.create_text(event.x, event.y, font=("等线", int(self.size)), text='text', fill=self.foreColor,tag=[self.tag[0]])
            self.what.set(1)
    
    def onLeftButtonMove(self,event):
        if self.yesno.get() == 0:
            return
        if self.what.get() == 1:
    
            self.lastDraw = self.canvas.create_line(self.X.get(), self.Y.get(), event.x, event.y,
                                        fill=self.foreColor,tag=[self.tag[0],'line'],width=5)
            self.X.set(event.x)
            self.Y.set(event.y)
        elif self.what.get() == 2:
            try:
                self.canvas.delete(self.lastDraw)
            except Exception:
                pass
    
            self.lastDraw = self.canvas.create_line(self.X.get(), self.Y.get(), event.x, event.y,
                                        fill=self.foreColor,tag=[self.tag[0],'line'],width=5)
        elif self.what.get() == 3:
    
            try:
                self.canvas.delete(self.lastDraw)
            except Exception:
                pass
            self.lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y,
                                            outline=self.foreColor,tag=[self.tag[0],'line'])
    
        elif self.what.get() == 5:
    
            self.lastDraw = self.canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10,
                                            outline=self.backColor,tag=[self.tag[0],'line'])
        elif self.what.get() == 6:
    
            try:
                self.canvas.delete(self.lastDraw)
            except Exception:
                pass
            self.lastDraw = self.canvas.create_oval(self.X.get(), self.Y.get(), event.x, event.y,
                                        fill=self.backColor, outline=self.foreColor,tag=[self.tag[0],'line'])
    
    def onLeftButtonUp(self,event):
        if self.what.get() == 2:
    
            self.lastDraw = self.canvas.create_line(self.X.get(), self.Y.get(), event.x, event.y, fill=self.foreColor,tag=[self.tag[0],'line'],width=5)
        elif self.what.get() == 3:
    
            self.lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline=self.foreColor,tag=[self.tag[0],'line'])
        elif self.what.get() == 6:
    
            self.lastDraw = self.canvas.create_oval(X.get(), Y.get(), event.x, event.y, outline=self.foreColor,tag=[self.tag[0],'line'])
        self.yesno.set(0)
        self.end.append(self.lastDraw)
    
    
    
    '''主菜单及其关联的函数'''
    
    
    def Save(self):
        self.getter(self.line)
    
    
    def Clear(self):
        self.canvas.delete('line')
        self.end = [50]
        self.lastDraw = 50
    
    
    def Back(self):
        print(self.end)
        print(self.lastDraw)
        if len(self.end) > 1:
            for i in range(self.end[-2], self.end[-1] + 1):
                print(i)
                self.canvas.delete(i)
            self.end.pop()
            self.lastDraw=self.end[-1]
        else:
            self.end = [50]
            self.lastDraw=50