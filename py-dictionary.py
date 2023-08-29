dictionary = {0:'Troll', 1:'Geek'}
for i in dictionary:
    print(i, dictionary[i])

#Dictionary Functions
dictionary[2] = 'name'
print(dictionary)
del dictionary[0]
print(dictionary)

element = dictionary.pop(2)
print(dictionary)
print(element)

e = {3:'Hello', 4:'World'}
dictionary.update(e)
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(1 in dictionary)
print('World' in dictionary.values())
