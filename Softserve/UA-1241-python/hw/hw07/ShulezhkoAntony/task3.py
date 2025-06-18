def count_characters(word):
  """
  Calculate the number of characters in a given string.
  """
  char_count = {}
  for char in word:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  return char_count
word = 'Hello!'
result = count_characters(word)
print(result)