import pyautogui

# текущие координаты курсора
print(pyautogui.position())

# Перемещение курсора на 100 пикселей вниз по диагонали за 0,5 секунд
pyautogui.moveTo(200, 200, 1)
print(pyautogui.position())

# Смещение курсора относительно левого верхнего угла экрана в течение секунды
pyautogui.moveTo(400, 400, 1)
print(pyautogui.position())

# Кликаем по указанным координатам
pyautogui.click(150, 300)
pyautogui.moveTo(500, 500, 1)
pyautogui.doubleClick(500, 500, duration=0.2) # duration - для плавного перемещения

# Печатаем текст на экран
pyautogui.typewrite("Привет!")

# В квадратных скобках можно указать клавиши, которые хотим нажать
pyautogui.typewrite(['enter', 'w'])

# Нажатие горячих клавиш на клавиатуре
# pyautogui.hotkey('winleft', 'r')
