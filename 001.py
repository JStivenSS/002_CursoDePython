set_a = {'col', 'mex', 'bra', 'arg', 'chi'}
set_b = {'col', 'mex', 'per', 'ecu', 'bol'}

set_c = set_a.union(set_b)

print(set_c)
print(set_a | set_b)

set_d = set_a.intersection(set_b)
print(set_d)
print(set_a & set_b)

set_e = set_a.difference(set_b)
print(set_e)
print(set_a - set_b)

set_f = set_a.symmetric_difference(set_b)
print(set_f)
print(set_a ^ set_b)


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries.union(northAm, centralAm, southAm)
print(new_set)
