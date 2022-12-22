r = open('text_for_mng.txt', encoding='utf-8')
r1 = set(r.read().split())
r.close

r = open('text_for_mng2.txt', encoding='utf-8')
r2 = set(r.read().split())
r.close

new = r1.intersection(r2)
print(new)

