# The basic premise of the game Gallows is to follow two rules:

# First character of next word must match last character of previous word.
# The word must not have already been said.
# Below is an example of a Gallows game:

# ['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']  #valid!

# ['motive', 'beach']  # invalid! - beach should start with "e"

# ['hive', 'eh', 'hive']  # invalid! - "hive" has already been said
# Write a Gallows class that has two instance variables:

# words: a list of words already said.
# game_over: a boolean that is true if the game is over.
# and two instance methods:

# play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).

# If it is valid, it adds the word to the words list, and returns the words list.
# If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
# restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".

# Examples:
# my_gallows = Gallows()
# my_gallows.play('apple') ➞ ['apple']
# my_gallows.play('ear') ➞ ['apple', 'ear']
# my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
# my_gallows.words ➞ ['apple', 'ear', 'rhino']
# # Words should be accessible.
# my_gallows.restart() ➞ "game restarted"
# # Words list should be set back to empty.
# my_gallows.play('hostess') ➞ ['hostess']
# my_gallows.play('stash') ➞ ['hostess', 'stash']
# my_gallows.play('hostess') ➞ "game over"
# # Words cannot have already been said.
# my_gallows.play('apple') ➞ ['apple']
# my_gallows.play('ear') ➞ ['apple', 'ear']
# my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
# # Corn does not start with an "o".
# my_gallows.play('corn') ➞"game over"
# my_gallows.words ➞ ['apple', 'ear', 'rhino']
# my_gallows.restart() ➞ "game restarted"
# my_gallows.words ➞ []

### **Перевод задачи на русский язык**  

### **Основная идея игры "Виселица" (`Gallows`)**  
# Игра строится на **двух правилах**:
# 1. **Первый символ следующего слова должен совпадать с последним символом предыдущего слова**.  
# 2. **Слово не должно повторяться** – оно должно быть новым.

# Примеры:
# ✔ `['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']` – **валидно!**  
# ✘ `['motive', 'beach']` – **невалидно** (слово `"beach"` должно начинаться с `"e"`)  
# ✘ `['hive', 'eh', 'hive']` – **невалидно** (`"hive"` уже было сказано ранее)  

# ### **Задание**  
# Создайте **класс `Gallows`**, который содержит:  
# 1. **Переменные экземпляра:**
#    - `words` – список уже сказанных слов.
#    - `game_over` – булево значение (`True`), если игра окончена.

# 2. **Методы экземпляра:**
#    - `play(word)`:  
#      - Принимает слово и проверяет его по **двум правилам**.
#      - Если слово **валидно**, оно добавляется в `words`, и метод возвращает список `words`.  
#      - Если слово **невалидно**, метод возвращает `"game over"` и устанавливает `game_over = True`.  
#    - `restart()`:  
#      - Сбрасывает `words` в `[]` и `game_over = False`.  
#      - Возвращает `"game restarted"`.

## **Код решения**
class Gallows:
    def __init__(self):
        """Game initialization: empty word list and 'game not over' status"""
        self.words = []
        self.game_over = False

    def play(self, word):
        """Adding a word to the game with two rules"""
        if self.game_over:
            return "game over"  # If the game is over, you can't continue

        # Check condition 2: the word must not be repeated
        if word in self.words:
            self.game_over = True
            return "game over"

        # Check condition 1: the first letter of the new word = the last letter of
        if self.words and self.words[-1][-1] != word[0]:
            self.game_over = True
            return "game over"

        # If the word matches all conditions, add it to the list
        self.words.append(word)
        return self.words

    def restart(self):
        """Restarting the game"""
        self.words = []  # Clear the word list
        self.game_over = False  # Update the game status
        return "game restarted"

## **Разбор кода, шаг за шагом**
### **1️⃣ `__init__`: инициализация**
# - `self.words = []` – создаёт пустой список слов.  
# - `self.game_over = False` – устанавливает начальное состояние игры (её можно продолжать).  

# ### **2️⃣ `play(word)`: обработка нового слова**
# 1. Если `game_over == True`, сразу возвращаем `"game over"`.  
# 2. Проверяем **повтор слов** (`word in self.words`).  
#    - Если слово уже есть – **завершаем игру** (`game_over = True`) и возвращаем `"game over"`.  
# 3. Проверяем **начальную/конечную буквы** (если есть предыдущее слово).  
#    - `self.words[-1][-1] != word[0]` → если буква не совпадает – завершаем игру.  
# 4. Если проверка пройдена – **добавляем слово в список**.  

### **3️⃣ `restart()`: сброс игры**
# - Очищает `self.words` (`[]`).  
# - Возвращает `game_over = False`.  
# - Выводит `"game restarted"` для информирования игрока.

## **✅ Финальная проверка решения**
game = Gallows()
print(game.play("word"))  # ['word']
print(game.play("dowry"))  # ['word', 'dowry']
print(game.play("yodel"))  # ['word', 'dowry', 'yodel']
print(game.play("leader"))  # ['word', 'dowry', 'yodel', 'leader']
print(game.play("righteous"))  # ['word', 'dowry', 'yodel', 'leader', 'righteous']
print(game.play("serpent"))  # ['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']

print(game.play("motive"))  # "game over" (не начинается на "t")

game.restart()  # "game restarted"

print(game.play("hive"))  # ['hive']
print(game.play("eh"))  # ['hive', 'eh']
print(game.play("hive"))  # "game over" (слово уже было использовано)

### **🔎 Итог**
# ✔ **Класс `Gallows` соответствует всем требованиям**:  
# - Проверяет **две игровые логики** (буквы + повторение).  
# - Позволяет **перезапускать игру**.  
# - Сохраняет **историю сказанных слов**.  
# - Держит `game_over` в актуальном состоянии.

# my_gallows = Gallows()
# my_gallows.play('apple')
# my_gallows.play('ear')
# my_gallows.play('rhino')
# my_gallows.words
# # Words should be accessible.
# my_gallows.restart()
# # Words list should be set back to empty.
# my_gallows.play('hostess')
# my_gallows.play('stash')
# my_gallows.play('hostess')
# # Words cannot have already been said.
# my_gallows.play('apple')
# my_gallows.play('ear')
# my_gallows.play('rhino')
# # Corn does not start with an "o".
# my_gallows.play('corn')
# my_gallows.words
# my_gallows.restart()
# my_gallows.words