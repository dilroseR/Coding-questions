# K Largest Pairs

"""
You are given two lists of integers nums0, nums1 and an integer k. 
Find k largest sum pairs where each pair contains one integer in nums0 and another in nums1, 
and return the sum of all of the pairs.

Constraints

0 ≤ n ≤ 100,000 where n is the length of nums0
0 ≤ m ≤ 100,000 where m is the length of nums1
0 ≤ k ≤ 100,000
0 ≤ k ≤ n * m


Example 1:

Input:-
nums0 = [5, 3, 9]
nums1 = [1, 2, 4]
k = 2

Output:-
24
"""

class Solution:
    def solve(self, nums0, nums1, k):
        lst=[]
        tot=0
        for i in nums0:
            for j in nums1:
                sum=0
                sum=i+j
                lst.append(sum)
        lst=sorted(lst,reverse=True)
        for i in range(0,k):
            tot=tot+lst[i]
        return tot