my_dikt = {'Dima': 2000, 'Nastya': 2001, 'Roma': 1976}
print(my_dikt)
print(my_dikt['Dima'])
print(my_dikt.get('Vlad'))
my_dikt.update({'Irina': 1975, 'Nadya': 1969})
meaning = my_dikt.pop('Nastya')
print(meaning)
print(my_dikt)

my_set = {1, 2, 3, 4, 1, 3 ,4 ,'Dima', 'Nastya', 'Roma', 'Dima'}
print(my_set)
my_set.add(6)
my_set.add('Vlad')
my_set.discard(1)
print(my_set)