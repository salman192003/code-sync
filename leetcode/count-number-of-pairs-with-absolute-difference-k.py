class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = 0

        for i in range(len(nums) - 1):
            
            for j in range (i + 1, len(nums)):

                if abs(nums[i] - nums[j]) == k:
                    pairs = pairs + 1

        return pairs