# Вариант 1
# def reverse_words(text):
#     tmp_str = text.split(" ")
#     tmp_lst = []
#     for word in tmp_str:
#         tmp_lst.append(word[::-1])
#
#     return " ".join(tmp_lst)

# Вариант 2
def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])

print(reverse_words('The quick brown fox jumps over the lazy dog.'))
