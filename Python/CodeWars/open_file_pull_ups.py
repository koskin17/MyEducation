while True:
    file = open("pull_ups.txt", "r+")
    n = int(input())

    listf = file.readlines()
    print(listf[n-1])

    file.close()

