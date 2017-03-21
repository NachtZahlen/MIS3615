import math


def quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    else:
        return None, None

def my_abs(a):
    if a < 0:
        return -a
    else:
        return a

def main():
    a = float(input('please enter a number:'))
    b = float(input('please enter a number:'))
    c = float(input('please enter a number:'))
    sol_1, sol_2 = quadratic(a, b, c)
    if sol_1:
        print('Results are: {} and {}.'.format(sol_1, sol_2))
    else:
        print('No Real Number Solution.')


if __name__ == '__main__':
    main()
