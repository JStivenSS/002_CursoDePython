numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = []

for i in numbers:
    numbers2.append(i * 2)
print(numbers)
print(numbers2)

numbers3 = list(map(lambda x: x * 2, numbers))
print(numbers3)

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(numbers_1)
print(numbers_2)
print(result)
