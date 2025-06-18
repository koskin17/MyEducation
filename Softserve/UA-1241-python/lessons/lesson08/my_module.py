def my_print():
    print("my_module")


print("out","my_module")


if __name__ == "__main__":
    print(f"{__name__=}", f"{__file__=}", f"{dir()=}")