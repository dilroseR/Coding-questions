#Check If a String Contains All Binary Codes of Size K

"""
Given a binary string s and an integer k.
Return True if every binary code of length k is a substring of s. Otherwise, return False.
"""
 

def hasAllCodes(s,k):

        for i in range(0,2**k):
            if bin(i)[2:].zfill(k) not in s:
                return False
        return True

print("Enter the string of binary digits: ")
s=input()
print("Enter the size: ")
k=int(input())
ans=hasAllCodes(s,k)
print(ans)