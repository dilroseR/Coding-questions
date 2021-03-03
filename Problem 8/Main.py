# Set Mismatch

"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

"""
Constraints:-
2 <= nums.length <= 104
1 <= nums[i] <= 104
"""

def findErrorNums(nums):
        ans=[]
        nums.sort()
        last=nums[len(nums)-1]
        
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])
                break
        for i in range(1,last+2):
            if i in nums:
                continue
            else:
                ans.append(i)
                break
        print(ans)

res=[]
print("Enter the set's elements:")
nums=input().split(" ")
for i in nums:
	i=int(i)
	res.append(i)
findErrorNums(res)

	