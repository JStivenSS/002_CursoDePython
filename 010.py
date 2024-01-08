def increment(x):
    return x + 1


# incrementV2 = lambda x: x + 1
def incrementV2(x): return x + 1


def high_ord_func(x, func):
    return x + func(x)


# hegh_ord_func_V2 = lambda x, func: x + func(x)
def hegh_ord_func_V2(x, func): return x + func(x)


result = high_ord_func(2, increment)

print(result)

result2 = hegh_ord_func_V2(2, incrementV2)
print(result2)

result3 = hegh_ord_func_V2(2, lambda x: x + 2)
print(result3)

result4 = hegh_ord_func_V2(2, lambda x: x * 2)
print(result4)
