'''
easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(nums):
        d = {}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]=2
                
        return list(d.keys())[list(d.values()).index(1)]

###
for testcase in [[2,2,1], [4,1,2,1,2], [1]]:
    print(Solution.singleNumber(testcase))