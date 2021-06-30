# Inverse Factorial

"""
Given a positive integer a, return n such that n! = a. 
If there is no integer n that is a factorial, then return -1.

Constraints:
0 < a < 2 ** 31
"""

import math
class Solution:
    def solve(self, a):
        i,num=0,1
        L=[]
        while i < a :
            i=math.factorial(num)
            L.append(i)
            num+=1
        if a in L :
            return L.index(a)+1
        else :
            return -1
        