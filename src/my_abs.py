def my_abs(number):
    n = float(number)
    if n < 0:
        absolute_value = -n
        print('the absolute value is {}.'.format(absolute_value))
    else:
        print('You should enter a negative number. Yes, this is how I define my_abs!')


my_abs(input('Please enter a negative value: '))


