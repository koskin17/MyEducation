def count_characters(s):
    #dictionary 
    char_count = {}
    
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1    
    return char_count

input_string = "hello"