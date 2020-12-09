"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time

start = time.time()
n = 2000000
# n=10
b = [1] * n

ans = 0
for i in range(2, n):
    if b[i]:
        ans += i
        if i * i < n:
            for j in range(i * i, n, i):
                b[j] = 0
print(ans)

end = time.time()

print("use second", end - start)
