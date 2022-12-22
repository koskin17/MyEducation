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
    Метод askyesno возвращает True или False
    '''
    answer = messagebox.askokcancel("Выход", "Закрыть программу?")
    if answer:
        root.destroy()

def open_file():
    '''
    Метод для открытия файла filedialog.askopenfilename возвращает
    путь к файлу
    '''
    file_path = filedialog.askopenfilename(title = "Выбор файла",
                                           filetypes = (("Текстовые файлы (*.txt)", "*.txt"),
                                                        ("Все файлы", "*.*")))
    if file_path:
       t.delete('1.0', END)
       file = open(file_path, encoding = 'utf-8')
       t.insert('1.0', file.read())
       file.close()
       '''
       Для проверки состояния файла использовать метод closed.
       Он возвращает False, если файл открыт
       '''
       print(file.closed)

def save_file():
    file_path = filedialog.asksaveasfilename(title = "Сохранение файла",
                                           filetypes = (("Текстовые файлы (*.txt)", "*.txt"),
                                                        ("Все файлы", "*.*")))
    file = open(file_path, 'w', encoding = 'utf-8')
    text = t.get('1.0', END)
    file.write(text)
    file.close()
    

def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']

# File
file_menu = Menu(main_menu, tearoff = 0)
file_menu.add_command(label = "Открыть", command = open_file)
file_menu.add_command(label = "Сохранить", command = save_file)
file_menu.add_separator()
file_menu.add_command(label = "Выход", command = notepad_quit)
main_menu.add_cascade(label = "Файл", menu = file_menu)

# Theme
theme_menu = Menu(main_menu, tearoff = 0)
theme_menu_sub = Menu(theme_menu, tearoff = 0)
theme_menu_sub.add_command(label = "Light Theme", command = lambda: change_theme('light'))
theme_menu_sub.add_command(label = "Dark Theme", command = lambda: change_theme('dark'))

theme_menu.add_cascade(label = "Оформление", menu = theme_menu_sub)
theme_menu.add_command(label = "О программе", command = about_program)
main_menu.add_cascade(label = "Разное", menu = theme_menu)

f_text = Frame(root)
f_text.pack(fill = BOTH, expand = True)

theme_colors = {
    "dark": {
        "text_bg": "#343D46",
        "text_fg": "#fff",
        "cursor": "#EDA756",
        "select_bg": "#4E5A65"},
    "light": {
        "text_bg": "#fff",
        "text_fg": "#000",
        "cursor": "#8000FF",
        "select_bg": "#777"}

    }

t = Text(f_text, bg = theme_colors['dark']['text_bg'],
         fg = theme_colors['dark']['text_fg'],
         font = ("Courier New", 12), padx = 10, pady = 10,
         wrap = WORD, insertbackground = theme_colors['dark']['cursor'],
         selectbackground = theme_colors['dark']['select_bg'],
         width = 10, spacing3 = 10)
t.pack(fill = BOTH, expand = True, side = LEFT)

scroll = Scrollbar(f_text, command = t.yview)
scroll.pack(fill = Y, side = LEFT)
t.config(yscrollcommand = scroll.set)

root.mainloop()
