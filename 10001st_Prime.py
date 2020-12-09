"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

"""we know that pi(n),means count of prime  pi(N)~N/ln(N)"""

import time
import math

start = time.time()
ans = [2, 3, 5, 7, 11, 13]

i = 14
inx = 6

while True:
    isPrime = True
    right_range = int(math.sqrt(i))
    for j in ans:
        if j > right_range:
            break
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        ans.append(i)
        inx += 1
        if 10001 == inx:
            print("ans", i, ans[:10])
            break
    i += 1

end = time.time()
print("use second", end - start)
