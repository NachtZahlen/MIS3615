[10, 20, 30]

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print(AFC_east[0])
# numbers = [42, 123]
# empty = []
# print(AFC_east, numbers, empty)

# total_count = 0
# for team in AFC_east:
#     print(team, len(team))
#     total_count += len(team)
#
# print('total count is', total_count)

# AFC_east[3] = 'New York Giants'
# print(AFC_east)
#
# print(AFC_east[1:3])
#
# print('Miami Dolphins' in AFC_east)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby', 'On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[2][2])
print(L[1][2][1])




numbers = [2, 0, -3]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)




my_list = ['spam', 1,
           ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants'],
           [1, 2, 3]
           ]
print(len(my_list))
print(len(my_list[2]))
