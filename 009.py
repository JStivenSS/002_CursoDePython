def increment(x):
    return x + 1


def incrementV2(x): return x + 1


result = increment(5)
print(result)

result2 = incrementV2(5)
print(result2)


# full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
def full_name(
    name, last_name): return f'Full name is {name.title()} {last_name.title()}'


text = full_name('daniel', 'garcia gutierres')
print(text)
