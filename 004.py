
import random
countries = ['col', 'mex', 'bra', 'arg', 'chi']
population = {i: random.randint(1, 100) for i in countries}
print(population)

newDict = {country: i for (country, i) in population.items() if i > 50}
print(newDict)


print(sum(i for i in newDict.values()))

text = 'Hola, soy José Alexander y me gusta programar en Python'
unique = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique)

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension
even_numbers_v2 = [number for number in numbers if number % 2 == 0]

print('v2 =>', even_numbers_v2)
