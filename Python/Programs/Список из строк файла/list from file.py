from tkinter import *
'''
Модули диалоговых окон необходимо импортировать отдельно.
'''
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('800x600+350+100')

main_menu = Menu(root)
root.config(menu = main_menu)

def about_program():
    '''
    Вывод всплывающего окна.
    Используется метод messagebox с его 4 основными методами:
    - showerror;
    - showwarning;
    - showinfo.
    '''
    messagebox.showinfo("About notepad", "Программа Notepad Version 0.0.1")
##    '''
##    Второй варинат записи - с именованными аргументами
##    '''
##    messagebox.showerror(title = "About notepad", message = "Программа Notepad Version 0.0.1")

def notepad_quit():
    '''
    Для выхода из программы или закрытия окна программы
    используется метод destroy().
    Для уточнение перед выходом используется messagebox с методами.
    Метод askquestion возвращает строку "yes" или "no"
    Метод askokcancel возращает True или False
    Метод askyesno воз�