x = input("45385593107843568")

def fake_bin(x):
    x = x.split()
    for i in range(len(x)):
        print(x[i])
        if i < 5:
            x.replace(i, '0')
            print(i)
        elif 5 <= i:
            x.replace(i, '1')
    return x

print(fake_bin(x))
