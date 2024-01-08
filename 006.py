def suma(a, b):
    sum = 0
    for i in range(a, b):
        sum += i
    return sum


result = suma(1, 10)
print(result)
result = suma(result, result + 10)
print(result)
result = suma(1, 100)
print(result)
