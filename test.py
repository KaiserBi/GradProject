import tkinter as tk
from tkinter import font
root = tk.Tk()
a=font.families(root)
text=[]
for i in a:
    tk.Label(root,text=i,font=(i,10)).pack()
root.mainloop()