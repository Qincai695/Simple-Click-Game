from tkinter import *
from tkinter.messagebox import showinfo
from random import randint
from time import time
root=Tk()
rx=int(root.geometry().split('+')[1])
ry=int(root.geometry().split('+')[1])
p=0
initflag=False
running=False
st=0
gt=10
def updatec():
    global running,st,initflag,fid,br,p,rx,ry
    rx=int(root.geometry().split('+')[1])
    ry=int(root.geometry().split('+')[1])
    if running:
        br.config(text=str(p)+' | '+str(10-(time()-st))[:5])
    else:
        br.config(text='0 | Click to Start')
    if time()-st>=gt and initflag and running:
        root.after_cancel(fid)
        running=False
        initflag=False
        br.config(state='disabled')
        rx=round(root.winfo_screenwidth()/2)
        ry=round(root.winfo_screenheight()/2)
        root.geometry('120x30'+'+'+str(rx)+'+'+str(ry))
        br.config(text=str(p)+' | '+'Click to restart')
        showinfo('Message','You click '+str(p)+' times in '+str(gt)+' seconds!')
        br.config(state='normal')
    else:
        fid=root.after(100,updatec)
def right():
    global p,st,initflag,running,fid
    if not initflag:
        initflag=True
        running=True
        fid=root.after(10,updatec)
        st=time()
        p=0
    if running:
        rx=int(root.geometry().split('+')[1])
        ry=int(root.geometry().split('+')[1])
        rx+=randint(-30,30)
        ry+=randint(-30,30)
        root.geometry('120x30'+'+'+str(rx)+'+'+str(ry))
        p+=1
def close():
    global running
    if not running:
        exit()
br=Button(root,command=right,text='0 | Click to Start',width=17)
br.pack(fill='both')
root.resizable(False,False)
root.attributes('-topmost', 'true')
root.protocol('WM_DELETE_WINDOW',close)
root.mainloop()