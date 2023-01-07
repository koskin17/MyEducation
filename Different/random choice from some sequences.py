# При помощи модуля random и метода choice можно из нескольких последовательностей выбирать элементы
# в случайном порядке
import random

nouns = ["puppy", "car", "rabbit", "girl", "monkey"]
verbs = ["runs", "hits", "jumps", "drives", "barfs"]
adv = ["crazily", "dutifully", "foolishly", "merrily", "occasionally"]

tmp_lst = [nouns, verbs, adv]
print("Вариант один: ", " ".join([random.choice(_) for _ in tmp_lst]))
print("Вариант два: ", " ".join([random.choice(_) for _ in tmp_lst]))
print("Вариант три: ", " ".join([random.choice(_) for _ in tmp_lst]))
