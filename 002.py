numbers = []
for i in range(1, 11):
    numbers.append(i*2)
print(numbers)

# List comprehension
numbers2 = [i*2 for i in range(1, 11)]
print(numbers2)

# List comprehension with conditionals

numbers3 = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers3.append(i*2)
print(numbers3)

numers4 = [i*2 for i in range(1, 11) if i % 2 == 0]
print(numers4)
