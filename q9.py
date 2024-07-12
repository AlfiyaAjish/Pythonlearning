'''Check if a decimal integer is a palindrome.
Given number like 1, 121, 78987 or 323, output is true.
Given number like -1, 12, 76, 1234556 output is false.'''
import math
a=-1
if a>0:
    b=math.floor(math.log10(a))+1
    print(b)
    count=math.floor((b+1)/2)
    while a>0:
        if (a%10)==(a//pow(10,b-1)):
            count-=1
            a=(a%pow(10,b-1))//10
            b=b-2
    if count==0:
        print('palindrome')
    else:
        print('not palindrome')
else:
    print('not palindrome')
    
