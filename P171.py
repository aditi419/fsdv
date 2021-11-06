from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.title('P171')
root.geometry('500x500')

australia_image = ImageTk.PhotoImage(Image.open('australia.jpg'))
japan_image = ImageTk.PhotoImage(Image.open('japan.jpg'))
usa_image = ImageTk.PhotoImage(Image.open('usa.jpg'))
india_image = ImageTk.PhotoImage(Image.open('india.jpg'))

australia_label = Label(root,text='Australia')
australia_label.place(relx=0.3,rely=0.2,anchor=CENTER)
australia_map = Label(root,image=australia_image)
australia_map.place(relx=0.3,rely=0.35,anchor=CENTER)
australia_time = Label(root)

japan_label = Label(root,text='Japan')
japan_label.place(relx=0.75,rely=0.2,anchor=CENTER)
japan_map = Label(root,image=japan_image)
japan_map.place(relx=0.75,rely=0.35,anchor=CENTER)
japan_time = Label(root)

usa_label = Label(root,text='USA')
usa_label.place(relx=0.3,rely=0.5,anchor=CENTER)
usa_map = Label(root,image=japan_image)
usa_map.place(relx=0.3,rely=0.65,anchor=CENTER)
usa_time = Label(root)

india_label = Label(root,text='Japan')
india_label.place(relx=0.75,rely=0.2,anchor=CENTER)
india_map = Label(root,image=india_image)
india_map.place(relx=0.75,rely=0.35,anchor=CENTER)
india_time = Label(root)

class Australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime('%H:%M:%S')
        australia_time['text'] = 'Time: ' + str(current_time)
        
class Japan():
    def times(self):
        home=pytz.timezone('Japan/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime('%H:%M:%S')
        Japan_time['text'] = 'Time: ' + str(current_time)

obj_australia = Australia()
obj_japan = Japan()

australia_btn = Button(root,text='Show Time',command=obj_australia.times)
australia_btn.place(relx=0.25,rely=0.92,anchor=CENTER)

japan_btn = Button(root,text='Show Time',command=obj_japan.times)
japan_btn.place(relx=0.25,rely=0.92,anchor=CENTER)

mainloop()

