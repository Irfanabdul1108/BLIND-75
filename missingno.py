# platform - leetcode
#link - https://leetcode.com/problems/missing-number/description/
# concept - finding missing number using bit manipulation


class Solution:
    def hammingWeight(self, n: int) -> int:
        m=bin(n)[2:]
        return m.count('1')
        

