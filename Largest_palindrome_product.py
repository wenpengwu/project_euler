'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

x1,x2=999,999
found_max=False
max_ans=0
for i in range(999,99,-1):
    for j in range(999,i-1,-1):
        tmp =i*j
        tmp_int = tmp
        tmp = str(tmp)
        if tmp==tmp[::-1]:
            max_ans = max(tmp_int,max_ans)
print(max_ans)




