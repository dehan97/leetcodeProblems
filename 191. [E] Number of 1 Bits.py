'''
Easy

Write a function that takes an unsigned integer and returns the number of '1' bits 
it has (also known as the Hamming weight).
'''

class Solution:
    def hammingWeight(n):
        r = 0
        for i in str(bin(int(n))):
            if i=="1":
                r+=1
        return r

###        
for testcase in ["00000000000000000000000000001011", "00000000000000000000000010000000", "11111111111111111111111111111101"]:
    print(Solution.hammingWeight(testcase))
