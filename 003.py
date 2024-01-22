import random
dict = {}
for i in range(1, 5):
    dict[i] = i*2

print(dict)

dict2 = {i: i * 2 for i in range(1, 5)}
print(dict2)


countries = ['col', 'mex', 'bol', 'pe']
population = {}

for i in countries:
    population[i] = random.randint(1, 100)
print(population)

population2 = {i: random.randint(1, 100) for i in countries}
print(population2)


names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

newDict = {name: age for (name, age) in zip(nombre = names,edad = ages)}
print(newDict)
