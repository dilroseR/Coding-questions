# Detect Voter Fraud

"""
Given a two dimensional list of integers votes, 
where each list has two elements [candidate_id, voter_id], 
report whether any voter has voted more than once.

Example:
Input:- votes = [[3, 1],[3, 0],[3, 4],[3, 3],[3, 2]]
Output:- False
"""

class Solution:
    def solve(self, votes):
        lst=[]
        for i in range(0,len(votes)):
            lst.append(votes[i][1])
        a=list(set(lst))
        if len(a)==len(lst):
            return False
        else:
            return True