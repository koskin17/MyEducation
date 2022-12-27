import snowballstemmer

# С русским языком
rus = snowballstemmer.RussianStemmer()
print(rus.stemWord("Морские"))
print(rus.stemWord("Многосторонний"))
print(rus.stemWord("Западный"))
print(rus.stemWord("Предвзятый"))

# С английским языком
eng = snowballstemmer.EnglishStemmer()
print(eng.stemWord("Beautiful"))
print(eng.stemWord("collection"))
