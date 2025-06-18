def filter_words(st):
    line = " ".join(st.split())
    return line[0].upper() + line[1:].lower()