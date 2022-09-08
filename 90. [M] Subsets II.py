'''
medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution:
    def subsetsWithDup(nums):
        ans = set()
        for i in range(1<<len(nums)):
            sublist = ()
            for j in range(len(nums)):
                if (i&(1<<j)): #to check if ith bit of number i is set.
                    sublist += (nums[j],)
            ans.add(tuple(sorted(sublist)))
        return list(ans)

#testing
for testcase in [[1,2,2], [0]]:
    print(Solution.subsetsWithDup(nums=testcase))