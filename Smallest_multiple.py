"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import collections

ret = {2: 1, 3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}
ret_keys = list(ret.keys())
for i in range(2, 20):
    if i in ret:
        continue
    factors = []
    j = 0
    while j < len(ret_keys):
        if i % ret_keys[j] == 0:
            factors.append(ret_keys[j])
            i = i / ret_keys[j]
            if i == 1:
                break
        else:
            j += 1
    cnt = collections.Counter(factors)
    for k, v in cnt.items():
        ret[k] = max(ret[k], v)
ans = 1
for k, v in ret.items():
    ans *= k ** v
print(ans)
