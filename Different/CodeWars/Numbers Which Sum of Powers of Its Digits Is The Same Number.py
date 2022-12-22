# Not considering number 1, the integer 153 is the first integer having this property: the sum
# of the third-power of each of its digits is equal to 153.
# Take a look: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
#
# The next number that experiments this particular behaviour is 370 with the same power.
#
# Write the function eq_sum_powdig(),
# that finds the numbers below a given upper limit hMax (inclusive) that fulfills this property but
# with different exponents as the power for the digits.
#
# eq_sum_powdig(hMax, exp): ----> sequence of numbers (sorted list) (Number one should not be considered).
#
# Let's see some cases:
#
# eq_sum_powdig(100, 2) ----> []
#
# eq_sum_powdig(1000, 2) ----> []
#
# eq_sum_powdig(200, 3) ----> [153]
#
# eq_sum_powdig(370, 3) ----> [153, 370]

def eq_sum_powdig(hmax, exp):
    lst = []
    tmp = 0
    for number in range(hmax + 1):
        for i in range(len(str(number))):
            tmp += int(str(number)[i]) ** exp

        if tmp == number and tmp not in [0, 1]:
            lst.append(number)

        tmp = 0

    return lst


print(eq_sum_powdig(370, 3)) # [153]
