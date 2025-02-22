gen_exp = (x**2 for x in range(5))

for value in gen_exp:
    print(value)

even_sum = sum(x for x in range(100) if x%2==0)
print(even_sum)