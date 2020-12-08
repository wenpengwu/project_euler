'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


'''
let MAX_VALUE=600851475143
max prime factor <= sqrt(MAX_VALUE)
'''
import math
MAX_VALUE = 600851475143

'''
Prime Gap
'''
n=math.ceil(math.sqrt(MAX_VALUE))+1
isPrime =[1]*n

for i in range(2,n):
    if isPrime[i] and i*i<n:
        for j in range(i*i,n,i):
            isPrime[j]=0

for i in range(n-1,2,-1):
    if isPrime[i] and MAX_VALUE%i==0:
        print(i)
        break