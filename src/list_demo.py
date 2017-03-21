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

# print(L[0][0])
# print(L[2][2])
# print(L[1][2][1])

numbers = [2, 0, -3]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
#
# print(numbers)

numbers.append(100)
print(numbers)

numbers.remove(0)
print('after removing:', numbers)

numbers.pop(0)
print('after popping 0:', numbers)

team = 'New England Patriots has a lot of great players and a great coach.'
words = team.split()

for word in words:
    print(word)

print(len(words))

s = 'spam-spam-spam'
t = s.split('-')
print(t)
