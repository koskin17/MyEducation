#Task3.
#Write a function that calculates the number of characters included in
#given string
#• input: "hello"
#• output: {"h":l, "e":1,"l":2,"o":1}

def count(calt):
   
    dict = {}
    for char in calt:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

print(count("hello")) 
