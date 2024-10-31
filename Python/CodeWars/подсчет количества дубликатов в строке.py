''' Нужно в полученной строке посчитать кол-во дубликатов и вывести наибольшее число '''
text = 'Indivisibilities'

def duplicate_count(text):
    text = text.lower()
    amount = 0
    for symbol in text:
        if text.count(symbol) >= 2:
            if text.count(symbol) > amount:
                amount = text.count(symbol)
    return amount
        

print(duplicate_count(text))
