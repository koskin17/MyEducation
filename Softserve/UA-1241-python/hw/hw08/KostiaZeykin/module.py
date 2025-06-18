# """Task 1"""
#
# def say_greeting(name):
#     print(f"Hello {name}")
#
#
# if __name__ == "__main__":
#     print("Hello world!")
#
"""Task 2"""

FREEZING_POINT = None
BOILING_POINT = None


def print_water_state(temperature):
    if temperature <= FREEZING_POINT:
        print("Solid")
    elif FREEZING_POINT < temperature < BOILING_POINT:
        print("Liquid")
    else:
        print("Gas")
