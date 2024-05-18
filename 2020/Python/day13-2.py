f = [i for i in open("input13.txt", "r")]

timestamp = int(f[0])
buses = [i for i in f[1].rstrip().split(",") if i != 'x']
buses1 = [int(f[1].rstrip().split(",")[i]) - i for i in range(len(f[1].rstrip().split(","))) if f[1].rstrip().split(",")[i] != 'x']

t = int(max(buses))

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print(buses)
print(buses1)

print(chinese_remainder([int(i) for i in buses], buses1))
