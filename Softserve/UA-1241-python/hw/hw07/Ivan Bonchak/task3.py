def cout_chen(a):
    char_cout ={}

    for b in a:
        if b in char_cout:
            char_cout[b] += 1
        else:
            char_cout[b] =1
    return char_cout

r = cout_chen("hello")
print(r)


