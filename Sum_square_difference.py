"""

The sum of the squares of the first ten natural numbers is,

1^2+2^2...+10^2=383

The square of the sum of the first ten natural numbers is,
(1+2..+10)^2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

one_sum_to_100 = (100 + 1) * 50  # 1+2...+100
# one_sum_to_100 = (10+1)*5
SUP = 101
# SUP = 11
ans = 0
for i in range(1, SUP):
    ans += i * (one_sum_to_100 - i)

print(ans)
