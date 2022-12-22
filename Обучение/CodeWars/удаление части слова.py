'''
В полученном массиве слов нужно из каждого слова,
содержащего rotten удалить это слово и само слово записать
с маленькой буквы
'''
bag_of_fruits = ["apple","rottenBanana","apple"]

def remove_rotten(bag_of_fruits):
    for fruit in range(len(bag_of_fruits)):
        if bag_of_fruits[fruit].startswith('rotten'):
            bag_of_fruits[fruit] = bag_of_fruits[fruit].replace('rotten', '').lower()
    return bag_of_fruits

print(remove_rotten(bag_of_fruits))
