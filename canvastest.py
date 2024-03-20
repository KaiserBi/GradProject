import time
import tkinter
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog
from PIL import Image, ImageTk, ImageGrab
 
def center_window(w, h):
    app.winfo_screenwidth()
    app.winfo_screenheight()
    app.geometry('%dx%d' % (w, h+20))
 
app = tkinter.Tk()
app.title('轩氏画图')
x = 500
y = 500
center_window(x, y)
 
yesno = tkinter.IntVar(value=0)
what = tkinter.IntVar(value=1)
X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
 
foreColor = '#000000'
backColor = '#FFFFFF'
 
image = tkinter.PhotoImage()
canvas = tkinter.Canvas(app, bg='white', width=x, height=y)
canvas.create_image(x, y, image=image)
 
lastDraw = 0
end = [0]
size = "20"
 
def getter(widget):
    time.sleep(0.5)
    x=app.winfo_rootx()+20
    y=app.winfo_rooty()+60
    x1=x+widget.winfo_width()*2-70
    y1=y+widget.winfo_height()*2-20
    filename = tkinter.filedialog.asksaveasfilename(filetypes=[('.jpg', 'JPG')],
                                                    initialdir='C:\\Users\\lin042\\Desktop\\')
    img=ImageGrab.grab().crop((x, y, x1, y1))
    img=img.convert('RGB')
    img.save(filename)
 
def onLeftButtonDown(event):
    yesno.set(1)
    X.set(event.x)
    Y.set(event.y)
    if what.get() == 4:
        canvas.create_text(event.x, event.y, font=("等线", int(size)), text='text', fill=foreColor)
        what.set(1)
 
def onLeftButtonMove(event):
    global lastDraw
    if yesno.get() == 0:
        return
    if what.get() == 1:
 
        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor)
        X.set(event.x)
        Y.set(event.y)
    elif what.get() == 2:
        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
 
        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor)
    elif what.get() == 3:
 
        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y,
                                           outline=foreColor)
 
    elif what.get() == 5:
 
        lastDraw = canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10,
                                           outline=backColor)
    elif what.get() == 6:
 
        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_oval(X.get(), Y.get(), event.x, event.y,
                                      fill=backColor, outline=foreColor)
 
def onLeftButtonUp(event):
    global lastDraw
    if what.get() == 2:
 
        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
    elif what.get() == 3:
 
        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y, outline=foreColor)
    elif what.get() == 6:
 
        lastDraw = canvas.create_oval(X.get(), Y.get(), event.x, event.y, outline=foreColor)
    yesno.set(0)
    end.append(lastDraw)
 
 
canvas.bind('<Button-1>', onLeftButtonDown)
canvas.bind('<B1-Motion>', onLeftButtonMove)
canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
 
'''主菜单及其关联的函'''

def Save():
    getter(canvas)
 
 
def Clear():
    global lastDraw, end
    for item in canvas.find_all():
        canvas.delete(item)
    end = [0]
    lastDraw = 0
 
 
def Back():
    global end
    print(end)
    print(lastDraw)
    try:
        for i in range(end[-2], end[-1] + 1):
            canvas.delete(i)
        end.pop()
    except:
        end = [0]
 
 
btn=tkinter.Button(app,text="",command=Back).pack()
 
app.mainloop()