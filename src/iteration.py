# s = 0
#
# for i in range(1001):
#     print('s=', s, 'i=', i)
#     s = s + i
#
# print(s)

# calculate the sum of all the odd numbers from 0 to 1000
# s = 0
# for i in range(1000):
#     if i % 2 == 0:
#         print('s=', s, 'i=', i)
#         # new_s = s + i
#         # s = new_s
#         s = s + i
#
# print(s)
from time import sleep

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        sleep(1)

    print('Blastoff!')

countdown(10)




