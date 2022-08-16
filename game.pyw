from random import randint
from tkinter import *
import time


max_targets = 20
x=0
y=0
t=0
h=0


def restart():
  btns.place_forget()
  scoref.place_forget()
  global t
  global max_targets
  global h
  h = 0
  score.config(text = h) 
  max_targets = int(input.get())
  t = time.time()
  x= randint(100, 400)
  y= randint(100, 400)
  btnc.place(x=x,y=y)

def start():
  btns.place_forget()
  global t
  global max_targets
  max_targets = int(input.get())
  t = time.time()
  x= randint(100, 400)
  y= randint(100, 400)
  btnc.place(x=x,y=y)


def stop():
   try: 
    btnc.place_forget()    
    global t
    time_taken =  round(time.time() - t)
    scoref.config(text= f'Time taken to hit {h} targets = {time_taken}sec')
    scoref.place(x=150,y=230)
    btns.config(command=restart)
    btns.place(x=230,y=250)
   except Exception: 
        input.delete(0, END)
        input.insert(0, 'Error! Enter a number please!')
        return

def btnpress():
    try:
       text = score["text"]
       result = int(text) + 1
       global h
       h = result
       score.config(text = result) 
       if( h == max_targets): 
         return stop()
       x= randint(100, 400)
       y= randint(100, 400)
       btnc.place(x=x,y=y)       
    except Exception: 
        score.config(text = 'Error') 
        return

root = Tk()
root.title('Calculator')
root.geometry('500x500')

text = Label(root, text='Number of targets')
text.config(bg='#58D3F7')
text.place(x=45,y=0)
input = Entry(root)
input.config(bg='#58D3F7',width=5)
input.place(x=150,y=0,width=215)
input.delete(0,END)
input.insert(0,max_targets)
scoret = Label(root, height = 1, width = 4, text='Score')
scoret.config(bg='#58D3F7')
scoret.place(x=230,y=30)
score = Label(root, height = 1, width = 4, text='0')
score.config(bg='#58D3F7')
score.place(x=230,y=50)
btns = Button(root, width= 5, text='Start', command=start)
btns.config(bg='Red')
btns.place(x=230,y=230)
btnc = Button(root, width= 5, height = 3, text='Click', command=btnpress)
btnc.config(bg='yellow')
scoref = Label(root)

root.mainloop()