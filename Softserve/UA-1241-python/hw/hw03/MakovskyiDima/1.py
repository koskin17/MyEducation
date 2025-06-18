python_philosophy = """
    Python's philosophy, often encapsulated in the Zen of Python, emphasizes simplicity and readability. 
    One of its core principles is that "explicit is better than implicit."
    This means that code should be clear and understandable rather than relying on hidden or obscure behaviors. Additionally, "Simple is better than complex," 
    suggesting that straightforward solutions are preferred over complicated ones. Lastly, "There is never just one obvious way to do it," 
    acknowledging that while there are guidelines, Python allows flexibility and creativity in coding."""

count_better = python_philosophy.count(" better ")
count_never = python_philosophy.count(" never ")
count_is = python_philosophy.count(" is ")

print(f"{count_better=}\n{count_never=}\n{count_is=}")

print(python_philosophy.upper())

python_philosophy_replace = python_philosophy.replace("i", "&")

print(python_philosophy_replace)