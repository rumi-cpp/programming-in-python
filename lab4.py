base = int(input("Base: "))
exp = int(input("Exponent: "))

result = 1
for i in range(exp):
    result *= base
print(base, "^", exp, "=", result)