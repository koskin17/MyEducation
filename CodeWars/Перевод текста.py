# импортировать библиотеку
from translate import Translator

# указать язык 
translator = Translator(to_lang="Hindi")

# набрать сообщение
translation = translator.translate('Hello!!! Welcome to my class')

# вывести перевод сообщения
print(translation)
