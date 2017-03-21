# grades = dict()
# grades['Andrea'] =95
#
# # print(grades)
#
# grades['Arpit'] = 76
# grades['Brian'] = 90

grades = {'Andrea': 95, 'Arpit': 76, 'Brian': 90, 'Shankar': 60}


# print(grades)
#
# print(grades['Brian'])
# print(grades['Shankar'])
#
# grades['Shankar'] = 65
# print(grades)
#
# print(len(grades))
#
# print('Shankar' in grades)
#
# print(65 in grades.values())

def histogram(s):
    d = dict()
    for c in s:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    return d


name = 'Ganesan Shankaranarayanan'
print(histogram(name))

json_example = {'class': {'student_1': {'name': 'Shankar', 'id': 1},
                          'student_2': {'name': 'Arpit', 'id':2}},
                'year': 2016
                }

print(len(json_example))

print(json_example['class']['student_2'] )



