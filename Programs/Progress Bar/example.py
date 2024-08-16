##from tkinter import *
##root = Tk()
##def getV(root):
##    a = scale1.get()
##    print ("Значение", a) 
##scale1 = Scale(root,orient=HORIZONTAL,length=300,from_=50,to=80,tickinterval=5,
##               resolution=5)
##button1 = Button(root,text=u"Получить значение")
##scale1.pack()
##button1.pack()
##button1.bind("<Button-1>",getV)
##root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
pb = ttk.Progressbar(root, length=100)
pb.pack()
pb.start(100)
root.mainloop()
