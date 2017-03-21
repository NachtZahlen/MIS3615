team = 'New England Patriots'

letter = team[0]

# print(letter)
# print(team[1])

# print(len(team))

# print(team[-1])



# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs these names in order:

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)

team = 'New England Patriots'
# print(team[:11])
# print(team[12:])
# print(team[:])

# new_team = team[:12] +'Seahawks'
# print(new_team)
#
# print(team)

# print(team[::-1])


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'E'))

def count_letter(word, letter_to_count):
    count = 0
    for letter in word:
        if letter == letter_to_count:
            count = count +1
    return count

team = team.lower()
print(team)
team = team.upper()
print(team)
print(count_letter(team, 'a'))

print('e' in team)
print('E' in team)

team = team.title()
print(team)


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

print(in_both(team, 'Andrea'))

