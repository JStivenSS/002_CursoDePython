items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'Sueter',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)


def add_taxes(item):
    new_items = item.copy()
    new_items['taxes'] = new_items['price'] * .19
    return new_items


new_items = list(map(add_taxes, items))

print(new_items)
print(items)


def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda item: item*2, numbers))
    return result


numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
