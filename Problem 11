# Palindromic Tree

# Given a binary tree root where each node contains a digit from 0-9, return whether its in-order traversal is a palindrome.


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        lst=[]
        def solve1(root):
            if root:
                solve1(root.left)
                lst.append(root.val)
                solve1(root.right)
        solve1(root)
        
        lst1=lst[::-1]
        if lst!=lst1:
            return False
        else:
            return True
