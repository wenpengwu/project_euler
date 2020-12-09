"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

start = time.time()

k = 10
m = 10
result = []
for k0 in range(1, k + 1):
    for m0 in range(2, m + 1):
        for n0 in range(1, m0):
            a = k0 * (m0 * m0 - n0 * n0)
            b = k0 * (2 * m0 * n0)
            c = k0 * (m0 * m0 + n0 * n0)
            if not {a, b, c} in result:
                result.append({a, b, c})
ans = []
for set1 in result:
    sum1 = 0
    if any(set1) > 1000:
        continue
    for i in set1:
        sum1 += i
    if 1000 % sum1 == 0:
        ans = set1
        break
r = 1
print(ans)
sum2 = 0
for i in ans:
    r *= i
    sum2 += i
r *= (1000 / sum2) ** 3

print(r)


end = time.time()

print("use second", end - start)
