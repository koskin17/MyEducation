from tkinter import *

root = Tk()
##root.geometry('600x400+1000+300')

##f = Frame(root)
##f.pack(pady = 10)
##
##btn_list = ['7','8','9',
##            '4','5','6',
##            '1','2','3',
##            '0']
##
##row = 0
##column = 0
##
##for i in btn_list:
##    if i == '0':
##        Button(f, text = i, padx = 10, pady = 5).grid(row = row, columnspan = 3)
##    else:
##        Button(f, text = i, padx = 10, pady = 5).grid(row = row, column = column)
##        column += 1
##        if column == 3:
##            column = 0
##            row += 1

##btn7 = Button(f, text = "7", padx = 10, pady = 5).grid(row = 0, column = 0)
##btn8 = Button(f, text = "8", padx = 10, pady = 5).grid(row = 0, column = 1)
##btn9 = Button(f, text = "9", padx = 10, pady = 5).grid(row = 0, column = 2)
##
##btn4 = Button(f, text = "4", padx = 10, pady = 5).grid(row = 1, column = 0)
##btn5 = Button(f, text = "5", padx = 10, pady = 5).grid(row = 1, column = 1)
##btn6 = Button(f, text = "6", padx = 10, pady = 5).grid(row = 1, column = 2)
##
##btn1 = Button(f, text = "1", padx = 10, pady = 5).grid(row = 2, column = 0)
##btn2 = Button(f, text = "2", padx = 10, pady = 5).grid(row = 2, column = 1)
##btn3 = Button(f, text = "3", padx = 10, pady = 5).grid(row = 2, column = 2)
##
##btn0 = Button(f, text = "0", padx = 10, pady = 5).grid(row = 3, column = 0, columnspan = 3)

l_user = Label(root, text = "Login:").grid(row = 0, column = 0, padx = 10, sticky = E)
'''
Если в атрибуте sticky указать W+E, к примеру, то виджет растянется на всю дилну
'''
e_user = Entry(root).grid(row = 0, column = 1, columnspan = 2, padx = 10, sticky = W+E)

l_pass = Label(root, text = "Password:").grid(row = 1, column = 0, padx = 10, sticky = E)
e_pass = Entry(root, show = '*').grid(row = 1, column = 1, columnspan = 2, padx = 10, sticky = W+E)

btn_login = Button(root, text = "Вход", padx = 5).grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
btn_reg = Button(root, text = "Регистрация:", padx = 5).grid(row = 2, column = 1)
btn_fogot = Button(root, text = "Забыли пароль", padx = 5).grid(row = 2, column = 2, padx = 10)

root.mainloop()
