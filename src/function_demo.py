def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

# repeat_lyrics()

def print_twice(some_name):
    print(some_name)
    print(some_name)


# print_twice('Andrea')
# print_twice('Babson')
#
# name = 'Anna'
# print_twice(name)

# def give_me_a_break():
#     str1 = 'break'
#     return str1
#
# print(give_me_a_break())


def give_me_a_break():
    str1 = 'break'
    print('I test whether this will be executed or not.')
    return str1
    # print('another break')

# print(give_me_a_break())

def another_function(s):
    print_twice(s)
    print_twice(s)

another_function(give_me_a_break())
