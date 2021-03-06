# 342. Power of Four
# ttungl@gmail.com
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example:
# Given num = 16, return true. Given num = 5, return false.

# Follow up: Could you solve it without loops/recursion?


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # sol 1:
        # runtime: 37ms
        if num <= 0:
            return False
        while num%4==0:
            num/=4
        return num==1
    
        # sol 2: follow-up
        # runtime: 51ms
        return num > 0 and (num & (num-1)==0) and (num-1)%3==0
    
        