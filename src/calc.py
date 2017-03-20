# print(2017 - 1998)
# print(2**10)
# minutes = 42
# seconds = 42
#
# print('The time duration is', minutes * 60 + seconds, 'seconds.')

#
# r = 5
# jess = (4 / 3) * r ** 3 * math.pi
# print(jess)

# len_of_number = len(str(2 ** 1000000)) # How many digits in a really BIG number?
# print(len_of_number)
#
# import random
#
# print(random.random())
#
# print(random.choice(['Jess', 'Andrea', 'Lucy']))

import math


def quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    else:
        print('No real number solution.')
        return None


# solutions = quadratic(1, -2, 5)
#
# if solutions is not None:
#     print(solutions)

a = float(input('please enter a number:'))
b = float(input('please enter a number:'))
c = float(input('please enter a number:'))
solutions = quadratic(a, b, c)

if solutions is not None:
    print(solutions)
