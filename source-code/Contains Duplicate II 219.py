# 219. Contains Duplicate II
# ttungl@gmail.com
# Given an array of integers and an integer k, find out whether there are two distinct 
# indices i and j in the array such that nums[i] = nums[j] and the absolute difference 
# between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # sol 1:
        # key: use dict store {v:i}.
        # check if it meets, v in d and i-d[v]<=k.
        # time O(n)
        # runtime: 45ms
        if k < 0: 
        	return False
        d = collections.defaultdict(int)
        for i,v in enumerate(nums):
            if v in d and i - d[v] <= k: 
                return True
            d[v] = i 
        return False
        

        